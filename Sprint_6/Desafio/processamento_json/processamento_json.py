import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime

# Parâmetros do job
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

#  Inicialização do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída
source_file = args['S3_INPUT_PATH']
output_path = args['S3_TARGET_PATH']

# Leitura do JSON
df = spark.read.option("encoding", "UTF-8").json(source_file)

# Conversão da coluna de data de string para tipo date
df = df.withColumn('release_date', F.to_date(
    F.col("release_date"), 'yyyy-MM-dd'))

#  Remoção de duplicatas por ID e registros com valores nulos
df = df.dropDuplicates(subset=["id"]).dropna()

# Extração da data (ano, mês, dia) a partir do caminho S3
data_separada = source_file.strip("/").split("/")
ano = (data_separada[-3])
mes = (data_separada[-2])
dia = (data_separada[-1])

# Adiciona coluna de data ano,mes e dia de extração para particionamento
df = (
    df.withColumn("ano", F.lit(ano))
      .withColumn("mes", F.lit(mes))
      .withColumn("dia", F.lit(dia))
)

# Escrita final no s3 particionado por ano, mes e dia
df.write.partitionBy("ano", "mes", "dia").parquet(output_path)

# FIM do job
job.commit()
