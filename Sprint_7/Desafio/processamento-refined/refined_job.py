import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from awsglue.job import Job

# Leitura dos parâmetros passados na execução do job
args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'LOCAL_INPUT_PATH',    # Caminho dos dados IMDb (parquet)
    'TMDB_INPUT_PATH',     # Caminho dos dados TMDB (parquet)
    'S3_TARGET_PATH'       # Caminho onde os resultados serão salvos
])

# Inicialização do contexto Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura dos caminhos parametrizados
source_file_local = args['LOCAL_INPUT_PATH']
source_file_tmdb = args['TMDB_INPUT_PATH']
output_path = args['S3_TARGET_PATH']

# Leitura dos dados TMDB e IMDB(em formato parquet)
df_tmdb = spark.read.parquet(source_file_tmdb)
df_local = spark.read.parquet(source_file_local)

# Filtro para garantir que os dados tenham valores válidos e recentes
df_tmdb = df_tmdb.filter(
    (F.col("revenue") > 0) &
    (F.col("budget") > 0) &
    (F.col("vote_count") > 0) &
    (F.col("popularity") > 0) &
    (F.col("release_date") >= F.lit("1970-01-01").cast("date"))
)

# Define os campos que serão usados para aplicar o filtro de percentil
campos = ["revenue", "budget", "vote_count", "popularity"]
percentil = 0.2
valores = {}

# Calcula o valor do percentil 20% para cada campo
for campo in campos:
    valor = df_tmdb.approxQuantile(campo, [percentil], 0.01)[0]
    valores[campo] = valor

# ========================
# ETAPA DE ENRIQUECIMENTO
# ========================

# Aplica os filtros com base nos valores de percentil e calcula o ROI
df_tmdb = df_tmdb.filter(
    (F.col("revenue") >= valores["revenue"]) &
    (F.col("budget") >= valores["budget"]) &
    (F.col("vote_count") >= valores["vote_count"]) &
    (F.col("popularity") >= valores["popularity"])
).withColumn("roi", F.round((F.col("revenue") - F.col("budget")) / F.col("budget"), 1)) \
 .filter("roi > 0")

# Renomeia a coluna id para id_filmes
df_tmdb = df_tmdb.withColumnRenamed("id", "id_filme")

# Realiza o join entre os dados do TMDB e IMDb usando o imdb_id como chave
df_geral = df_tmdb.join(df_local, df_tmdb.imdb_id == df_local.id, "inner")

# Seleciona e renomeia colunas para padronizar
df_geral = df_geral.select(
    F.col("id_filme"),
    F.col("imdb_id"),
    F.col("title").alias("titulo_no_brasil"),
    F.col("tituloPrincipal").alias("titulo_principal"),
    F.col("tituloOriginal").alias("titulo_original"),
    F.col("release_date").alias("data_lancamento"),
    F.col("numeroVotos").alias("qtd_votos_imdb"),
    F.col("notaMedia").alias("nota_media_imdb"),
    F.col("vote_count").alias("qtd_votos_tmdb"),
    F.col("vote_average").alias("nota_media_tmdb"),
    F.col("popularity").alias("popularidade"),
    F.col("budget").alias("orcamento"),
    F.col("revenue").alias("receita"),
    F.col("roi"),
    F.col("nomeArtista").alias("nome_artista"),
)

# ============================
# Criação da dimensão de artistas
# ============================
df_artista = df_geral.select("nome_artista").distinct() \
    .withColumn("id_artista", F.monotonically_increasing_id()) \
    .select("id_artista", "nome_artista")

# ============================
# Criação da dimensão de data
# ============================
df_data = df_geral.select(F.col("data_lancamento")).distinct()
df_data = df_data.withColumn("ano", F.year("data_lancamento")) \
    .withColumn("mes", F.month("data_lancamento")) \
    .withColumn("dia", F.dayofmonth("data_lancamento")) \
    .withColumn("trimestre", F.when(F.month("data_lancamento").isin([1, 2, 3]), "T1")
                .when(F.month("data_lancamento").isin([4, 5, 6]), "T2")
                .when(F.month("data_lancamento").isin([7, 8, 9]), "T3")
                .otherwise("T4")) \
    .withColumn("decada", (F.col("ano") / 10).cast("int") * 10) \
    .withColumn("id_data", F.monotonically_increasing_id()) \
    .select("id_data", "data_lancamento", "ano", "mes", "dia", "trimestre", "decada")

# ============================
# Criação da dimensão de filmes
# ============================
df_filmes = df_geral.select(
    "id_filme", "imdb_id", "titulo_no_brasil", "titulo_principal", "titulo_original"
).distinct()

# ============================
# Criação da tabela fato
# ============================
df_fato = df_geral.select(
    "id_filme", "orcamento", "receita", "roi",
    F.round("nota_media_tmdb", 1).alias("nota_media_tmdb"),
    F.round("nota_media_imdb", 1).alias("nota_media_imdb"),
    "qtd_votos_tmdb", "qtd_votos_imdb", "popularidade",
    "data_lancamento", "nome_artista"
)

# Realiza o join com as dimensões de artista e data para obter id_artista e id_data
df_fato = df_fato.join(df_artista, df_fato.nome_artista ==
                       df_artista.nome_artista, "inner")
df_fato = df_fato.join(df_data, df_fato.data_lancamento ==
                       df_data.data_lancamento, "inner")

# Seleciona as colunas finais da tabela fato
df_fato = df_fato.select(
    "id_filme",
    "id_data",
    "id_artista",
    "orcamento",
    "receita",
    "roi",
    "nota_media_tmdb",
    "nota_media_imdb",
    "qtd_votos_tmdb",
    "qtd_votos_imdb",
    "popularidade"
)

# ============================
# Escrita das tabelas em formato Parquet no S3
# ============================
df_fato.write.mode("overwrite").parquet(f"{output_path}/fato_filmes_artista")
df_data.write.mode("overwrite").parquet(f"{output_path}/dim_data")
df_artista.write.mode("overwrite").parquet(f"{output_path}/dim_artista")
df_filmes.write.mode("overwrite").parquet(f"{output_path}/dim_filmes")

# Finaliza o job Glue
job.commit()
