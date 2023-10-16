from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').appName('Test').getOrCreate()
print("Spark object is created")

rdd = spark.sparkContext.parallelize([1,2,3])
print(rdd.first())