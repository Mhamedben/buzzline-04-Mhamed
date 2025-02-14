import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Initial sentiment data
sentiment_data = ['positive', 'neutral', 'negative', 'positive', 'neutral', 'positive']

# Function to update sentiment data (simulating real-time data changes)
def update_sentiment_data():
    sentiments = ['positive', 'neutral', 'negative']
    sentiment_data.append(random.choice(sentiments))  # Simulate new sentiment
    # Keep the list size fixed to the last 10 data points
    if len(sentiment_data) > 10:
        sentiment_data.pop(0)

# Function to animate the pie chart
def animate(i):
    # Update sentiment data
    update_sentiment_data()

    # Count occurrences of each sentiment
    positive_count = sentiment_data.count('positive')
    neutral_count = sentiment_data.count('neutral')
    negative_count = sentiment_data.count('negative')

    # Data for pie chart
    counts = [positive_count, neutral_count, negative_count]
    labels = ['Positive', 'Neutral', 'Negative']

    # Clear the previous plot to update
    ax.clear()

    # Create a pie chart
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107', '#F44336'])

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Set a title for the chart
    ax.set_title('Real-Time Sentiment Distribution - Mhamed')

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(7, 7))

# Animate the plot (updates every 1000 milliseconds, or 1 second)
ani = animation.FuncAnimation(fig, animate, interval=1000)

# Display the real-time pie chart
plt.show()