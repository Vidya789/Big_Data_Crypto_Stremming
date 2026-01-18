from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from pyspark.sql import SparkSession

# Spark session
spark = SparkSession.builder \
    .appName("SparkToInfluxDB") \
    .getOrCreate()

# Sample Spark DataFrame
data = [("BTC", 47000), ("ETH", 3200)]
columns = ["symbol", "price"]
df = spark.createDataFrame(data, columns)

# InfluxDB config
url = "http://localhost:8086"
token = "skVN1pRn1PP5lNhxwbeMMmztdDmXqIEjJiyQU4Sw02NGABG76BvnhOlo6MzCu8aQm_vp541qIM8e84di3ma9GQ=="
org = "ESILV"
bucket = "crypto"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Write Spark DataFrame to InfluxDB
for row in df.collect():
    point = Point("crypto_test") \
        .tag("symbol", row["symbol"]) \
        .field("price", row["price"])
    write_api.write(bucket=bucket, record=point)

client.close()
print("Data written to InfluxDB successfully!")
