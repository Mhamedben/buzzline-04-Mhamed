# Real-Time Sentiment Analysis with Kafka

## Overview

This project involves real-time sentiment analysis using Kafka to consume messages, process them, and visualize the sentiment distribution over time. The producer sends JSON-formatted messages to a Kafka topic, and the consumer processes these messages to compute and visualize sentiment insights.

## New Consumer - Sentiment Distribution by Author

### What does it do?
The newly added consumer listens to Kafka messages and tracks the sentiment data by each author. It calculates the average sentiment for each author and displays the sentiment distribution in real-time using a **pie chart**. The pie chart is updated dynamically as new messages arrive, allowing you to observe how different authors contribute to overall sentiment trends.

### Focused Insight:
The consumer provides insights into the **sentiment distribution by author**. Specifically, it:
- Tracks the sentiment of each author's messages.
- Computes the average sentiment for each author over time.
- Visualizes the distribution of sentiment by author using a pie chart.

### Visualized Chart:
We visualize a **real-time pie chart** showing the sentiment distribution for each author. Each slice of the pie represents an author, with the size of the slice corresponding to their average sentiment score. The chart is updated continuously to reflect changes in the authors' sentiment values as new messages are processed. This chart helps to identify which authors contribute more positive or negative sentiment in the message stream.

### Why is it interesting?
This visualization is interesting because it allows you to track the tone of messages in real-time, providing valuable insights into user behavior and emotional trends. It can be used to analyze how authors influence the overall sentiment in a discussion or content stream.

---

## Running the Project

### Running the Project Producer (No Modifications Needed)

1. **Start Kafka and Zookeeper** (if not already running):
   ```bash
   # Start Zookeeper
   zookeeper-server-start.sh config/zookeeper.properties
   # Start Kafka server
   kafka-server-start.sh config/server.properties
