import json
from collections import defaultdict
from kafka import KafkaConsumer
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import threading

# Kafka Configuration
TOPIC = "project_json"
KAFKA_SERVER = "localhost:9092"

# Data Storage
author_sentiments = defaultdict(list)  # Store sentiment values per author

# Consumer Setup
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    """Function to consume messages from Kafka and update sentiment data by author."""
    print("Waiting for messages...")
    for message in consumer:
        data = message.value
        author = data.get("author", "Unknown")  # Get the author of the message
        sentiment = data.get("sentiment", 0)  # Get the sentiment value
        
        # Add the sentiment value to the corresponding author
        author_sentiments[author].append(sentiment)

        print(f"Updated author sentiments: {author_sentiments}")

def calculate_average_sentiment_by_author():
    """Function to calculate the average sentiment for each author."""
    average_sentiment_by_author = {}
    for author, sentiments in author_sentiments.items():
        if sentiments:
            average_sentiment_by_author[author] = sum(sentiments) / len(sentiments)
    return average_sentiment_by_author

def animate(i):
    """Function to update the real-time pie chart of sentiment distribution by author."""
    plt.cla()
    
    # Calculate average sentiment for each author
    average_sentiment_by_author = calculate_average_sentiment_by_author()
    
    # Separate authors and their average sentiments for plotting
    authors = list(average_sentiment_by_author.keys())
    avg_sentiments = list(average_sentiment_by_author.values())
    
    # Create a pie chart
    plt.pie(avg_sentiments, labels=authors, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title("Real-Time Sentiment Distribution by Author - Mhamed M")
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is drawn as a circle.

# Main
if __name__ == "__main__":
    # Start Kafka consumer in the background
    threading.Thread(target=consume_messages, daemon=True).start()

    # Start Matplotlib animation for pie chart
    fig = plt.figure()
    ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
    plt.show()