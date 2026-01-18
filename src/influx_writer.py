from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import random

# InfluxDB config
url = "http://localhost:8086"
token = "skVN1pRn1PP5lNhxwbeMMmztdDmXqIEjJiyQU4Sw02NGABG76BvnhOlo6MzCu8aQm_vp541qIM8e84di3ma9GQ=="
org = "ESILV"
bucket = "crypto"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

print("Starting BTC writer...")

while True:
    price = random.uniform(40000, 45000)

    point = (
        Point("crypto_price")
        .tag("symbol", "BTC")
        .field("price", price)
    )

    write_api.write(bucket=bucket, record=point)
    print("BTC price written:", price)

    time.sleep(5)  # 🔑 This creates continuous line
