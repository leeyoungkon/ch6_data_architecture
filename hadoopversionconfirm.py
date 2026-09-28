from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

print("Spark version :", spark.version)

print(
    "Hadoop version:",
    spark.sparkContext._jvm.org.apache.hadoop.util.VersionInfo.getVersion()
)