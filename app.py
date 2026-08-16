import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Customer Service Chatbot")

st.title("🤖 Customer Service Chatbot")
st.write("Chat with the assistant and see how it responds to your sentiment.")

sentiment_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

message = st.text_input("Enter your message:")

if st.button("Send"):
    if message.strip():

        result = sentiment_model(message)[0]
        sentiment = result["label"]
        score = result["score"]

        if sentiment == "positive":
            response = "Thank you! 😊 We're happy to know that you are satisfied with our service."

        elif sentiment == "negative":
            response = "I'm sorry to hear that. 😔 We understand your concern and will try our best to help you."

        else:
            response = "Thank you for contacting us. How can I assist you further?"

        st.write("### Sentiment")
        st.write(sentiment.capitalize())

        st.write("### Confidence")
        st.write(f"{score:.2%}")

        st.write("### Chatbot Response")
        st.write(response)

    else:
        st.warning("Please enter a message.")