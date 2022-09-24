from pyspark.sql import SparkSession
spark = SparkSession.builder\
    .appName('SparkByExamples')\
    .master('spark://spark-master:7077')\
    .getOrCreate()

#Creates Empty RDD
emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)
