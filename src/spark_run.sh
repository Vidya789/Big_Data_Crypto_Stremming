#!/bin/bash
echo "Starting Spark streaming in tmux..."

tmux new-session -d -s spark "cd ~/crypto_streaming && source venv/bin/activate && spark-submit spark_kafka_hdfs.py"

echo "Spark job started in tmux session: spark"
echo "To attach: tmux attach -t spark"

