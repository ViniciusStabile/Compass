import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as F

# @params: [JOB_NAME]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# 1
df = spark.read.option("header", "true") \
               .option("sep", ",") \
               .option("inferSchema", "true").csv(source_file)

# 2
print(df.schema)

# 3
df = df.withColumn("nome", F.upper(F.col("nome")))

# 4
print(df.count())

# 5
resultado_5 = df.groupBy("ano", "sexo").agg(
    F.sum("total").alias("Total")).orderBy(F.col("ano").desc())
resultado_5.show()

# 6
resultado_6 = (
    df.filter(F.col("sexo") == "F")
    .groupBy("nome", "ano")
    .agg(F.sum("total").alias("Total"))
    .orderBy(F.col("Total").desc())
    .limit(1)
)
resultado_6.show()

# 7
resultado_7 = (
    df.filter(F.col("sexo") == "M")
    .groupBy("nome", "ano")
    .agg(F.sum("total").alias("Total"))
    .orderBy(F.col("Total").desc())
    .limit(1)
)
resultado_7.show()

# 8
resultado_8 = df.groupBy("ano", "sexo").agg(
    F.sum("total").alias("Total")).orderBy(F.col("ano")).limit(10)
resultado_8.show()

df.write.mode("overwrite").partitionBy("sexo", "ano").json(target_path)

job.commit()
