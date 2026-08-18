# Medical Q&A Chatbot

## Overview

This project is a Medical Q&A Chatbot developed using the MedQuAD dataset. It retrieves relevant medical questions and answers using TF-IDF and cosine similarity and provides the results through a Streamlit web interface.

## Features

* Loads medical questions and answers from the MedQuAD dataset.
* Processes 16,407 medical Q&A pairs.
* Uses TF-IDF vectorization for question representation.
* Uses cosine similarity to find relevant questions.
* Performs Named Entity Recognition (NER) using spaCy.
* Provides an interactive Streamlit interface.
* Displays the best matching medical question, similarity score, and answer.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* spaCy
* Streamlit
* MedQuAD Dataset

## Project Structure

```text
Task2_Medical_QA/
│
├── data_loader.py
├── retriever.py
├── ner.py
├── app.py
├── README.md
├── requirements.txt
├── retrieval_test.png
├── ner_test.png
├── streamlit_test.png
└── venv/
```

## How It Works

1. The MedQuAD dataset is loaded.
2. Medical questions are extracted from the dataset.
3. TF-IDF converts the questions into numerical vectors.
4. Cosine similarity compares the user's question with the dataset questions.
5. The most relevant question and answer are returned.
6. spaCy performs entity recognition on medical text.
7. Streamlit provides the chatbot interface.

## Running the Project

Activate the virtual environment and install the required dependencies.

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application opens in a browser and allows the user to enter medical questions.

## Example Question

**What are the treatments for Adult Acute Lymphoblastic Leukemia?**

The system retrieves the most relevant question from the MedQuAD dataset and displays the corresponding answer.

## Testing and Evidence

The project was tested using:

* Retrieval testing
* Medical Entity Recognition testing
* Streamlit interface testing

Screenshots of the tests are included in the project folder as evidence.

## Note

This project is intended for educational purposes and should not be used as a substitute for professional medical advice.
