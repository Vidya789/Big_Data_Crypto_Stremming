from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, LongType

spark = SparkSession.builder.appName("KafkaToHDFS").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

schema = StructType() \
    .add("symbol", StringType()) \
    .add("price", DoubleType()) \
    .add("quantity", DoubleType()) \
    .add("trade_time", LongType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "crypto") \
    .load()

parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = parsed.writeStream \
    .format("parquet") \
    .option("checkpointLocation", "/crypto/parquet/checkpoint") \
    .option("path", "/crypto/parquet/data") \
    .option("checkpointLocation", "/crypto/checkpoints") \
    .outputMode("append") \
    .start()

query.awaitTermination()
