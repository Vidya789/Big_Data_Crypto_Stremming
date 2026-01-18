
This project implements a **real-time big data streaming pipeline** for cryptocurrency price data using:

- **Binance WebSocket API** - Live crypto data
- **Apache Kafka (KRaft mode)** - Message broker
- **Apache Spark Structured Streaming (YARN)** - Real-time processing
- **Hadoop HDFS (Parquet)** - Distributed storage
- **InfluxDB**-  Time-series database
- **Grafana** -  Monitoring & visualization

The pipeline ingests live crypto prices, processes them in real time, stores results in HDFS, and visualizes metrics through Grafana dashboards.


# Cluster Setup
Cluster Nodes and Roles


| **Node Name** | **Role**                                      |
|---------------|-----------------------------------------------|
| master        | Hadoop NameNode, Spark Driver, Kafka Broker  |
| worker        | Hadoop DataNode, Spark Executor              |
``

## Software Versions
- Hadoop: **3.7.1**
- Spark: **3.5.7**
- Kafka: **3.7.0 (KRaft mode)**
- InfluxDB: **2.7.5**
- Grafana: **12.3.0**
- Python: **3.12.3**
- Java: **OpenJDK 11.0.29**

## Full Pipeline Startup Checklist
We recommend **5 terminals** for smooth execution:

### **Terminal 1 – Hadoop (HDFS + YARN)**
```bash
start-dfs.sh
start-yarn.sh
jps   # Verify NameNode, DataNode, ResourceManager, NodeManager

Browser Verification:

HDFS UI - http://localhost:9870
YARN UI - http://localhost:8088

### **Terminal 2 – Kafka Broker (KRaft mode)**

cd /opt/kafka/kafka_2.13-3.7.0
bin/kafka-storage.sh random-uuid
bin/kafka-storage.sh format -t <CLUSTER_ID> -c config/kraft/server.properties
bin/kafka-server-start.sh config/kraft/server.properties

Create topic:

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic crypto --partitions 2 --replication-factor 1

### **Terminal 3 – Kafka Producer**

cd ~/kafka_project
source venv/bin/activate
nohup python producer.py &

### **Terminal 4 – Kafka Consumer**

cd ~/kafka_project
source venv/bin/activate
nohup python kafka_to_influx.py &

### **Terminal 5 – Spark Structured Streaming**

cd ~/crypto_streaming
spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \
  spark_kafka_hdfs.py

Browser Verification:

YARN UI - http://localhost:8088
Check HDFS output: /crypto/parquet/data

### **Terminal 6 – HDFS Check**
hdfs dfs -ls /crypto/parquet/data

Able to see multiple part-00000-*.snappy.parquet files.

InfluxDB & Grafana

InfluxDB UI → http://localhost:8086
Grafana UI → http://localhost:3000

###  Monitoring
Grafana dashboards visualize:

Hadoop memory usage
Spark job metrics
Real-time crypto data from InfluxDB

### ** Repository Structure**

big-data-project/
│── src/
│   ├── spark/spark_job.py
│   ├── kafka/producer.py
│   └── hadoop/hdfs_commands.sh
│── config/
│   ├── core-site.xml
│   ├── hdfs-site.xml
│   ├── yarn-site.xml
│   ├── spark-defaults.conf
│   └── server.properties
│── scripts/
│   ├── start-hadoop.sh
│   ├── start-spark.sh
│   ├── start-kafka.sh
│   └── run-job.sh
│── data/
│   ├── input/sample_data.csv
│   └── output/
│── monitoring/
│   └── grafana-dashboard.png
│── README.md
│── LICENSE

### ** License ** 
This project is licensed under the MIT License.


