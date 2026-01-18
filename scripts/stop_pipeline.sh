#!/bin/bash

echo "Stopping tmux sessions..."
tmux kill-session -t spark 2>/dev/null
tmux kill-session -t producer 2>/dev/null
tmux kill-session -t consumer 2>/dev/null
tmux kill-session -t kafka 2>/dev/null

echo "Stopping YARN apps..."
yarn application -kill $(yarn application -list | awk 'NR>2 {print $1}')
