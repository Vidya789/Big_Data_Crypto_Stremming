# Monitoring

Monitoring is a critical component of big data systems, especially for real-time data processing applications. In this project, monitoring is used to continuously observe system performance, data flow, and application health to ensure reliable and efficient processing of cryptocurrency streaming data.

## Monitoring Architecture

Kafka → Spark Streaming → InfluxDB → Grafana

## Metrics Monitored

### Kafka Metrics
- Messages per second
- Consumer lag
- Topic throughput

### Spark Streaming Metrics
- Batch processing time
- Streaming latency
- Executor CPU and memory usage

### System Metrics
- CPU usage
- Memory usage
- Disk utilization

## Tools Used
- Kafka
- Spark Streaming
- InfluxDB
- Grafana

## Conclusion

The monitoring framework provides real-time visibility into system performance and ensures reliability and scalability of the streaming pipeline.
