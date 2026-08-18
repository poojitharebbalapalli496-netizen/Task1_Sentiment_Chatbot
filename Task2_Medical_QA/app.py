import streamlit as st
from retriever import MedicalRetriever

st.title("Medical Q&A Chatbot")
st.write("Ask a medical question based on the MedQuAD dataset.")

retriever = MedicalRetriever()

question = st.text_input("Enter your medical question:")

if st.button("Get Answer"):
    if question:
        results = retriever.search(question, top_k=1)

        result = results[0]

        st.subheader("Best Matching Question")
        st.write(result["question"])

        st.subheader("Similarity")
        st.write(round(result["score"], 3))

        st.subheader("Answer")
        st.write(result["answer"])

    else:
        st.warning("Please enter a medical question.")