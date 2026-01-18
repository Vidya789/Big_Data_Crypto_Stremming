O
import json
from kafka import KafkaProducer
from websocket import WebSocketApp

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def on_message(ws, message):
    data = json.loads(message)
    trade = {
        "symbol": data["s"].lower(),
        "price": float(data["p"]),
        "quantity": float(data["q"]),
        "trade_time": data["T"]
    }
    producer.send("crypto", trade)
    print("Sent to Kafka:", trade)

def on_error(ws, error):
    print("WebSocket Error:", error)

def on_close(ws, code, msg):
    print("WebSocket closed")

def on_open(ws):
    print("Connected to Binance")

socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"
ws = WebSocketApp(socket,
                  on_open=on_open,
                  on_message=on_message,
                  on_error=on_error,
                  on_close=on_close)

ws.run_forever()
