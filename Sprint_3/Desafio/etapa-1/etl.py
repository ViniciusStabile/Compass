import pandas as pd


def limpar_coluna_numerica(df, *nomes_colunas):
    """
    Remove todos os caracteres não numéricos da coluna especificada e converte para float.

    :param df: DataFrame de entrada
    :param nome_coluna: Nome da coluna a ser limpa
    :return: DataFrame com a coluna convertida
    """
    for nome_coluna in nomes_colunas:
        df[nome_coluna] = df[nome_coluna].astype(str).str.replace(
            r'[^0-9]', '', regex=True).replace('', '0').astype(float)
    return df


def limpar_coluna_texto(df, *nomes_colunas):
    """
    Remove colchetes com conteúdo e caracteres especiais, mantendo apenas letras, números e espaços.

    :param df: DataFrame de entrada
    :param nome_coluna: Nome da coluna de texto a ser limpa
    :return: DataFrame com a coluna tratada
    """
    for nome_coluna in nomes_colunas:
        df[nome_coluna] = df[nome_coluna].str.replace(
            r'\[[^\]]*\]', '', regex=True).str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
    return df


def extrair_anos(df, coluna_origem='Year(s)', col_inicio='Start year', col_fim='End year'):
    """
    Extrai os anos de início e fim de uma coluna com intervalo de anos.
    Exemplo de entrada: '2023-2024' ou '2023'

    :param df: DataFrame de entrada
    :param coluna_origem: Nome da coluna com os anos no formato 'YYYY-YYYY' ou 'YYYY'
    :param col_inicio: Nome da nova coluna de início
    :param col_fim: Nome da nova coluna de fim
    :return: DataFrame com as colunas de ano de início e fim tratadas como inteiros
    """
    df[[col_inicio, col_fim]] = df[coluna_origem].str.split('-', expand=True)
    df[col_fim] = df[col_fim].fillna(df[col_inicio])
    df[col_inicio] = df[col_inicio].astype(int)
    df[col_fim] = df[col_fim].astype(int)
    return df


def remover_colunas(df, colunas):
    """
    Remove colunas especificadas de um DataFrame, ignorando as que não existirem.

    :param df: DataFrame de entrada
    :param colunas: Lista de colunas a remover
    :return: DataFrame sem as colunas especificadas
    """
    return df.drop(columns=[col for col in colunas if col in df.columns])


def salvar_csv(df, caminho_arquivo, index=False):
    """
    Salva um DataFrame como CSV.

    :param df: DataFrame a ser salvo
    :param caminho_arquivo: Caminho do arquivo CSV de saída
    :param index: Se True, inclui o índice no CSV
    """
    df.to_csv(caminho_arquivo, index=index)


def main():
    url = 'concert_tours_by_women.csv'
    df = pd.read_csv(url)

    df = limpar_coluna_numerica(
        df, 'Actual gross', 'Adjustedgross (in 2022 dollars)', 'Average gross')

    df = limpar_coluna_texto(df, 'Tour title')

    df = extrair_anos(df)

    colunas_remover = ['Peak', 'All Time Peak', 'Ref.', 'Year(s)']
    df = remover_colunas(df, colunas_remover)

    salvar_csv(df, 'volume/csv_limpo.csv')

    print(df)


if __name__ == "__main__":
    main()
