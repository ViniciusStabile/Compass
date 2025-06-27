import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from awsglue.context import GlueContext
from awsglue.job import Job

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


#  Definindo  o schema explícito dos dados CSV
schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", DoubleType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Leituda do arquivo CSV
df = spark.read.option("encoding", "UTF-8") \
    .csv(source_file, schema=schema, sep="|", header=True)

# Corrige coluna com nome errado
df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

#  Remoção de duplicatas e valores nuloes
df = df.dropDuplicates().dropna()

#  Escreve o resultado final no S3 em formato Parquet
df.write.mode("overwrite").parquet(output_path)

# FIM do job
job.commit()
