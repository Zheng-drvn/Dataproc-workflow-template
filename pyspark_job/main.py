from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# read csv with options
df = spark.read \
    .option("header", "true") \
    .csv("sample.csv")

print(df)
