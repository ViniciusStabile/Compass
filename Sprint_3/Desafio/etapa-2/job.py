import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def responder_q1(df: pd.DataFrame) -> str:
    agrupado_artista = df.groupby('Artist').agg({
        'Actual gross': ['count', 'mean']
    })

    agrupado_artista.columns = ['aparicoes', 'media_valor']
    agrupado_ordenado = agrupado_artista.sort_values(
        by=['aparicoes', 'media_valor'], ascending=[False, False])

    artista = agrupado_ordenado.head(1)
    nome = artista.index[0]
    aparicoes = artista['aparicoes'].values[0]
    media = artista['media_valor'].values[0]

    return (
        f"Q1 - A artista que mais aparece na lista é {nome}, com {aparicoes} turnês registradas e uma média de faturamento bruto por turnê de ${media:,.2f}."
    )


def responder_q2(df: pd.DataFrame) -> str:
    maior_media_faturamento = df.loc[df['Start year'] == df['End year']].sort_values(
        'Average gross', ascending=False).head(1)
    titulo = maior_media_faturamento['Tour title'].values[0]
    artista = maior_media_faturamento['Artist'].values[0]
    return (
        f"Q2 - A turnê que aconteceu dentro de um ano a que teve a maior média de faturamento bruto foi '{titulo}', realizada pelo(a) artista {artista}."
    )


def responder_q3(df: pd.DataFrame) -> str:
    df['preco_por_show_actual'] = df['Adjustedgross (in 2022 dollars)'] / \
        df['Shows']

    top3 = df[['Artist', 'Tour title', 'preco_por_show_actual']] \
        .sort_values('preco_por_show_actual', ascending=False).head(3)

    mensagens = []
    for i, row in top3.iterrows():
        artista = row['Artist']
        turne = row['Tour title']
        valor = row['preco_por_show_actual']
        mensagens.append(
            f"- Turnê '{turne}' do(a) artista {artista}, com valor por show de ${valor:,.2f}"
        )

    return "Q3 - Top 3 shows unitários mais lucrativos:\n" + "\n".join(mensagens)


def responder_q4(df: pd.DataFrame) -> str:
    agrupado_artista = df.groupby('Artist').agg({
        'Actual gross': ['count', 'sum']
    })
    agrupado_artista.columns = ['aparicoes', 'somatorio_faturamento']

    artista_top = agrupado_artista.sort_values(
        by=['aparicoes', 'somatorio_faturamento'], ascending=[False, False]).head(1)
    nome_artista = artista_top.index[0]

    df_artista = df[df['Artist'] == nome_artista]
    faturamento_ano = df_artista.groupby('Start year')['Actual gross'].sum()
    faturamento_ano = faturamento_ano / 1000000

    plt.figure(figsize=(10, 6))
    faturamento_ano.plot(kind='line', marker='o')
    plt.title(f'Faturamento Bruto por ano de turne - {nome_artista}')
    plt.xlabel('Ano')
    plt.ylabel('Faturamento Bruto (USD em milhões)')
    plt.grid(True)
    ticks = [round(y, 1) for y in plt.yticks()[0]]
    plt.yticks(ticks, [f'{t}M' for t in ticks])
    plt.xticks(faturamento_ano.index)
    plt.tight_layout()
    plt.savefig(f'Q4.png')
    plt.close()

    return f"Q4 - Gráfico salvo como Q4.png"


def responder_q5(df: pd.DataFrame) -> str:
    artistas_mais_shows = df[['Artist', 'Shows']] \
        .groupby('Artist').sum(numeric_only=True) \
        .sort_values(by='Shows', ascending=False) \
        .head(5).reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(artistas_mais_shows['Artist'], artistas_mais_shows['Shows'])
    plt.title('Q5 - Artistas com mais shows')
    plt.ylabel('Quantidade de Shows')
    plt.xlabel('Artista')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('Q5.png')
    plt.close()

    return 'Q5 - Gráfico salvo como Q5.png'


def main():

    url = 'volume/csv_limpo.csv'

    try:
        df = pd.read_csv(url)
        logging.info(f"Arquivo {url} carregado com sucesso.")
    except FileNotFoundError:
        logging.error(f"Arquivo {url} não encontrado.")
        return

    logging.info(responder_q1(df))
    logging.info(responder_q2(df))
    logging.info(responder_q3(df))
    logging.info(responder_q4(df))
    logging.info(responder_q5(df))


if __name__ == "__main__":
    main()
