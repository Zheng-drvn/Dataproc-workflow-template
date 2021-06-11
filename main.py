from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# read csv with options
spark.read \
    .option("header", "true") \
    .csv("some_input_file.csv")

