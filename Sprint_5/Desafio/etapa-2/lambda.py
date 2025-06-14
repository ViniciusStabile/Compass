import boto3
import pandas as pd
import requests
import io
import os
import json
import logging
import asyncio
from datetime import datetime

s3 = boto3.client('s3')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = 'vinicius-desafio-pb'
DATA_EXECUCAO = datetime.now().strftime('%Y/%m/%d')
OBJECT_KEY = f'Raw/Local/CSV/Movies/{DATA_EXECUCAO}/movies.csv'
API_KEY = os.getenv("API_KEY")
CAMADA = 'Raw'
ORIGEM = 'TMDB'
FORMATO = 'JSON'
ESPECIFICACAO = 'Movies'


def ler_csv_do_s3(bucket: str, key: str) -> pd.DataFrame:
    """Lê um arquivo CSV diretamente do S3 e carrega como DataFrame."""
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read()
    return pd.read_csv(io.BytesIO(content), sep='|')


def filtrar_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica filtros ao DataFrame para limitar os filmes que serão enriquecidos via API.
    Os critérios incluem ano de lançamento > 1900, votos > 10000 e gênero 'crime' ou 'war'.
    """
    df['anoLancamento'] = pd.to_numeric(df['anoLancamento'], errors='coerce')
    return df[
        (df['numeroVotos'] > 10000) &
        (df['anoLancamento'] > 1960) &
        (df['genero'].str.lower().str.contains('crime|war', na=False))
    ]


def extrair_ids(df_filtrado: pd.DataFrame) -> list[str]:
    """Extrai os IDs únicos do DataFrame filtrado."""
    return df_filtrado['id'].dropna().unique().tolist()


def list_ids(bucket_name: str, key: str) -> list[str]:
    """
    Lê o CSV do S3, filtra os dados e retorna uma lista de IDs para consulta na API TMDB.
    """
    try:
        df = ler_csv_do_s3(bucket_name, key)
        df_filtrado = filtrar_df(df)
        lista_ids = extrair_ids(df_filtrado)
        logger.info(f'Total de filmes para buscar no TMDB: {len(lista_ids)}')
        return lista_ids
    except Exception as e:
        logger.error(f'Erro ao listar IDs: {str(e)}')
        return []


async def extrair_info_filmes(
    id_list: list[str],
    api_key: str,
    max_concurrent_requests: int = 50
) -> tuple[list[dict], list[str]]:
    """
    Consulta a API do TMDB de forma assíncrona para obter dados de filmes.
    Retorna uma tupla contendo os dados limpos e uma lista de IDs com erro.
    """
    resultados = []
    ids_com_erro = []
    sem = asyncio.Semaphore(max_concurrent_requests)

    async def get_movie(movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"
        async with sem:
            try:
                response = await asyncio.to_thread(requests.get, url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    filme_detalhado = {
                        "id": data.get("id"),
                        "imdb_id": data.get("imdb_id"),
                        "title": data.get("title"),
                        "runtime": data.get("runtime"),
                        "release_date": data.get("release_date"),
                        "budget": data.get("budget"),
                        "revenue": data.get("revenue"),
                        "popularity": data.get("popularity"),
                        "vote_average": data.get("vote_average"),
                        "vote_count": data.get("vote_count"),
                    }
                    resultados.append(filme_detalhado)
                elif response.status_code == 404:
                    logger.warning(f"ID não encontrado: {movie_id}")
                    ids_com_erro.append(movie_id)
                elif response.status_code == 429:
                    logger.warning(f"Rate limit: {movie_id}")
                    await asyncio.sleep(2)
                    ids_com_erro.append(movie_id)
                else:
                    logger.warning(
                        f"Erro {response.status_code} para {movie_id}")
                    ids_com_erro.append(movie_id)
            except Exception as e:
                logger.error(f"Erro ao buscar {movie_id}: {str(e)}")
                ids_com_erro.append(movie_id)

    tasks = [get_movie(id) for id in id_list]
    await asyncio.gather(*tasks)
    return resultados, ids_com_erro


async def processar_em_lotes(
    ids: list[str],
    api_key: str,
    bucket_name: str,
    camada: str,
    origem: str,
    formato: str,
    especificacao: str
) -> None:
    """
    Processa os dados em lotes de 100 filmes.
    A cada lote, salva os resultados no S3 e acumula os erros para salvar no final.
    """
    batch_size = 100
    todos_ids_com_erro = []

    for i in range(0, len(ids), batch_size):
        lote_ids = ids[i:i + batch_size]
        lote_num = i // batch_size + 1

        dados_tmdb, ids_com_erro = await extrair_info_filmes(lote_ids, api_key)

        save_lote_to_s3(
            dados=dados_tmdb,
            bucket=bucket_name,
            lote_num=lote_num
        )

        todos_ids_com_erro.extend(ids_com_erro)

    if todos_ids_com_erro:
        erro_path_final = f"{camada}/{origem}/{formato}/{especificacao}/{DATA_EXECUCAO}/erros_geral.json"
        save_ids_com_erro(todos_ids_com_erro, bucket_name, erro_path_final)


def save_ids_com_erro(ids: list[int], bucket_name: str, caminho: str):
    """Salva os IDs com erro em um único JSON no S3."""
    if not ids:
        return
    buffer = io.StringIO()
    json.dump(ids, buffer)
    buffer.seek(0)
    s3.put_object(Bucket=bucket_name, Key=caminho, Body=buffer.getvalue())
    logger.info(f"{len(ids)} IDs com erro salvos em {caminho}")


def save_lote_to_s3(dados: list[dict], bucket: str, lote_num: int):
    """Salva um lote de dados TMDB no S3 em formato JSON."""
    if not dados:
        logger.warning(f"Nenhum dado para salvar no lote {lote_num}")
        return

    caminho = f"{CAMADA}/{ORIGEM}/{FORMATO}/{ESPECIFICACAO}/{DATA_EXECUCAO}/lote_{lote_num}.json"
    buffer = io.StringIO()
    for item in dados:
        buffer.write(json.dumps(item) + "\n")
    buffer.seek(0)
    s3.put_object(Bucket=bucket, Key=caminho, Body=buffer.getvalue())
    logger.info(f"{len(dados)} registros salvos no S3 em {caminho}")


def lambda_handler(event, context):
    """Função principal do Lambda. Orquestra leitura do CSV, enriquecimento e salvamento no S3."""
    try:
        ids = list_ids(BUCKET_NAME, OBJECT_KEY)
        if not ids:
            return {
                'statusCode': 200,
                'body': 'Nenhum ID encontrado para processar.'
            }

        asyncio.run(processar_em_lotes(ids, API_KEY, BUCKET_NAME,
                                       CAMADA, ORIGEM, FORMATO, ESPECIFICACAO))

        return {
            'statusCode': 200,
            'body': f'{len(ids)} filmes processados e salvos em lotes na estrutura {CAMADA}/{ORIGEM}/{FORMATO}/...'
        }

    except Exception as e:
        logger.error(f'Erro geral: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Erro ao executar Lambda: {str(e)}'
        }
