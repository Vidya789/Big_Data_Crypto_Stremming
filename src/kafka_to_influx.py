import json
from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point
import time

# Kafka Consumer
consumer = KafkaConsumer(
    'crypto',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# InfluxDB setup
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "ODHAI_-OXwijNQ229_DoLoKyXa5ySbdZj53kEmsSyhJ5Yd4bBb0kVYjW9Z8MtU0qigd1CkL41f42XBQ0YKVzjA=="
INFLUX_ORG = "ESILV"
INFLUX_BUCKET = "crypto"

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api()

print("Kafka consumer started, writing to InfluxDB...")

for message in consumer:
    trade = message.value
    timestamp_ns = int(trade["trade_time"] * 1_000_000)  # Binance ms → ns

    point = (
        Point("crypto_price")
        .tag("symbol", trade["symbol"])
        .field("price", trade["price"])
        .field("quantity", trade["quantity"])
        .time(timestamp_ns)
    )

    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
    print("Written to InfluxDB:", trade)
