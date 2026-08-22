# Task 1 - Sentiment Analysis Customer Service Chatbot

## Objective

The objective of this task is to integrate sentiment analysis into a customer service chatbot so that it can identify the emotion expressed in a user's message and provide an appropriate response.

## Problem Statement

Customer messages can express positive, negative, or neutral emotions. The chatbot should recognize these sentiments and respond appropriately to improve the customer interaction.

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- CardiffNLP Twitter-RoBERTa sentiment model

## Implementation

The chatbot uses a pretrained sentiment-analysis model through the Transformers pipeline. The user enters a message, and the model analyzes the message to identify its sentiment and confidence score.

Based on the detected sentiment, the chatbot provides a suitable customer-service response.

## Sentiment Categories

The chatbot handles three sentiment categories:

- Positive
- Negative
- Neutral

## Working Process

1. The user enters a customer message.
2. The message is sent to the sentiment-analysis model.
3. The model predicts the sentiment and confidence score.
4. The chatbot displays the detected sentiment.
5. The chatbot provides an appropriate response based on the sentiment.

## Testing

The application was tested with positive, negative, and neutral customer messages.

### Positive Test

Example:

"I am very happy with your service."

Expected sentiment: Positive

### Negative Test

Example:

"I am very disappointed with your service."

Expected sentiment: Negative

### Neutral Test

Example:

"I want to know the status of my order."

Expected sentiment: Neutral

## Results

The chatbot successfully analyzes user messages and provides sentiment-based customer-service responses.

## Challenges and Solutions

During implementation, the required Python libraries and pretrained sentiment-analysis model had to be configured correctly. The application was tested after setup to verify that sentiment detection and responses worked as expected.

## Future Improvements

Future versions can include conversation history, improved emotion recognition, personalized responses, multilingual support, and better handling of ambiguous customer messages.

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt