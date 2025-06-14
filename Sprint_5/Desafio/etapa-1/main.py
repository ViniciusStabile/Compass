import logging
import boto3
import os
from datetime import datetime
from botocore.exceptions import (
    ProfileNotFound,
    NoCredentialsError,
    BotoCoreError,
    EndpointConnectionError,
    ClientError,
    PartialCredentialsError
)

# --------------------- Configurações --------------------- #
BUCKET_NAME = 'vinicius-desafio-pb'
PROFILE_NAME = 'compass-sso'
DIRETORIO_ARQUIVOS = './dados'
DATA_EXECUCAO = datetime.now()
ORIGEM = 'Local'
CAMADA = 'Raw'
# --------------------------------------------------------- #

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


def s3_auth(profile_name: str) -> boto3.client:
    """
    Cria uma sessão autenticada com a AWS usando um profile local e retorna o client do S3 
    """
    logger.info('Autenticando na AWS...')
    try:
        session = boto3.Session(profile_name=profile_name)
        s3 = session.client('s3')
        s3.get_bucket_acl(Bucket=BUCKET_NAME)
        logger.info('Autenticação e verificação bem-sucedidas.')
        return s3
    except (ProfileNotFound, NoCredentialsError, PartialCredentialsError):
        logger.exception(" Problema com perfil ou credenciais AWS.")
    except EndpointConnectionError:
        logger.exception("Erro de conexão com o endpoint da AWS.")
    except ClientError as e:
        logger.exception(f"Erro do cliente AWS: {e}")
    except BotoCoreError as e:
        logger.exception(f"Erro geral da AWS: {e}")
    except Exception as e:
        logger.exception(f" Erro inesperado: {e}")


def gerar_key_s3(nome_arquivo: str) -> str:
    """
    Gera a key do S3 no padrão solicitado:
    <camada>/<origem>/<formato>/<especificacao>/<ano>/<mes>/<dia>/<arquivo>
    """
    nome_sem_extensao = os.path.splitext(os.path.basename(nome_arquivo))[0]
    especificacao = nome_sem_extensao.capitalize()
    formato = os.path.splitext(nome_arquivo)[1][1:].upper()

    key = f"{CAMADA}/{ORIGEM}/{formato}/{especificacao}/{DATA_EXECUCAO.year}/{DATA_EXECUCAO.month:02d}/{DATA_EXECUCAO.day:02d}/{nome_arquivo}"
    return key


def objeto_existe(s3: boto3.client, bucket_name: str, key: str) -> bool:
    """
    Verifica se um objeto com a key especificada já existe no bucket S3.
    """
    try:
        s3.head_object(Bucket=bucket_name, Key=key)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            return False
        else:
            logger.exception("Erro ao verificar existência do objeto.")
            raise


def upload_arquivo(s3: boto3.client, bucket_name: str, caminho_arquivo: str, key: str) -> None:
    """
    Realiza o upload de um arquivo local para o bucket S3 no caminho (key) especificado.
    """
    try:
        s3.upload_file(caminho_arquivo, bucket_name, key)
        logger.info(
            f"Upload concluído: {caminho_arquivo} → s3://{bucket_name}/{key}")
    except FileNotFoundError:
        logger.error(f" Arquivo local '{caminho_arquivo}' não encontrado.")
    except ClientError as e:
        logger.error(f" Erro do cliente AWS: {e.response['Error']['Message']}")
    except Exception as e:
        logger.exception(f" Erro inesperado durante upload: {e}")


def listar_objetos_bucket(s3: boto3.client, bucket_name: str) -> None:
    """
    Lista os objetos dentro do bucket.
    """
    logger.info(f"Listando objetos no bucket: {bucket_name}")
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                logger.info(f" - {obj['Key']}")
        else:
            logger.info("Bucket está vazio.")
    except Exception as e:
        logger.exception("Erro ao listar objetos do bucket.")


def main() -> None:
    s3 = s3_auth(PROFILE_NAME)
    if s3 is None:
        logger.error("Erro na autenticação. Encerrando execução.")
        return

    arquivos = [f for f in os.listdir(
        DIRETORIO_ARQUIVOS) if f.endswith('.csv')]
    if not arquivos:
        logger.warning("Nenhum arquivo .csv encontrado para upload.")
        return

    for arquivo in arquivos:
        caminho = os.path.join(DIRETORIO_ARQUIVOS, arquivo)
        key = gerar_key_s3(arquivo)

        if objeto_existe(s3, BUCKET_NAME, key):
            logger.warning(
                f"Arquivo já existe no bucket: {key}. Upload ignorado.")
            continue
        upload_arquivo(s3, BUCKET_NAME, caminho, key)

    listar_objetos_bucket(s3, BUCKET_NAME)


if __name__ == '__main__':
    main()
