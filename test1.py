from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Orders ETL")
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.5.0"
    )
    .config(
        "spark.hadoop.fs.s3a.endpoint",
        "http://localhost:9000"
    )
    .config(
        "spark.hadoop.fs.s3a.access.key",
        "admin"
    )
    .config(
        "spark.hadoop.fs.s3a.secret.key",
        "password"
    )
    .config(
        "spark.hadoop.fs.s3a.path.style.access",
        "true"
    )
    .config(
        "spark.hadoop.fs.s3a.connection.ssl.enabled",
        "false"
    )
    .getOrCreate()
)

print("Spark 시작")

df = spark.read.csv(
    "orders.csv",
    header=True,
    inferSchema=True
)

df.show()

df.write.mode("overwrite").parquet(
    "s3a://warehouse/raw/orders"
)

print("MinIO 저장 완료")

spark.stop()
print("Spark 종료")