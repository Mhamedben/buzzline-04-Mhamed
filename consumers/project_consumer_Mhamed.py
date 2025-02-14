import json
from collections import defaultdict
from kafka import KafkaConsumer
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Kafka Configuration
TOPIC = "project_json"
KAFKA_SERVER = "localhost:9092"

# Data Storage
message_counts = defaultdict(int)  # Store total message counts per category
sentiment_data = defaultdict(list)  # Store sentiment values per category

# Consumer Setup
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    """Function to consume messages from Kafka and update message counts and sentiment."""
    print("Waiting for messages...")
    for message in consumer:
        data = message.value
        category = data.get("category", "other")
        sentiment = data.get("sentiment", 0)
        
        # Increment the count for this category
        message_counts[category] += 1

        # Add the sentiment value to the corresponding category
        sentiment_data[category].append(sentiment)

        print(f"Updated message counts: {message_counts}")
        print(f"Updated sentiment data: {sentiment_data}")

def calculate_average_sentiment():
    """Function to calculate the average sentiment for each category."""
    average_sentiment = {}
    for category, sentiments in sentiment_data.items():
        if sentiments:
            average_sentiment[category] = sum(sentiments) / len(sentiments)
    return average_sentiment

def animate(i):
    """Function to update the real-time visualization of sentiment trends."""
    plt.cla()
    
    # Calculate average sentiment for each category
    average_sentiment = calculate_average_sentiment()
    
    # Separate categories and their average sentiments for plotting
    categories = list(average_sentiment.keys())
    avg_sentiments = list(average_sentiment.values())
    
    plt.plot(categories, avg_sentiments, marker='o', linestyle='-', color='b')
    plt.xlabel("Categories")
    plt.ylabel("Average Sentiment")
    plt.title("Real-Time Average Sentiment by Category - David Rodriguez")
    plt.xticks(rotation=45)

# Main
if __name__ == "__main__":
    # Start Kafka consumer in the background
    import threading
    threading.Thread(target=consume_messages, daemon=True).start()

    # Start Matplotlib animation
    fig = plt.figure()
    ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
    plt.show()