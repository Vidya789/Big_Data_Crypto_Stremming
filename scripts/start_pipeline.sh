#!/bin/bash

tmux new-session -d -s kafka "cd /opt/kafka/kafka_2.13-3.7.0 && bin/kafka-server-start.sh config/kraft/server.properties"

tmux new-session -d -s consumer "cd ~/crypto_streaming && source venv/bin/activate && python3 consumer.py"

tmux new-session -d -s producer "cd ~/crypto_streaming && source venv/bin/activate && python3 producer.py"

tmux new-session -d -s spark "cd ~/crypto_streaming && source venv/bin/activate && spark-submit spark_kafka_hdfs.py"
