# Task 3 - Dynamic Knowledge Base

## Overview

This project implements a dynamic knowledge base that allows information to be added, searched, updated, and deleted dynamically.

The system uses semantic search to retrieve relevant information based on the meaning of the user's query rather than only matching exact keywords.

## Features

- Add new knowledge dynamically
- Semantic search using sentence embeddings
- Retrieve Top-3 relevant results
- View all stored knowledge
- Update existing knowledge
- Delete knowledge
- Duplicate prevention
- Source/category metadata
- Knowledge base statistics
- Persistent ChromaDB storage
- Streamlit web interface

## Technologies Used

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- Hugging Face
- NumPy

## Project Structure

```text
Task3_Dynamic_Knowledge_Base/
│
├── app.py
├── knowledge_updater.py
├── knowledge_search.py
├── knowledge_manager.py
├── clean_database.py
├── requirements.txt
├── README.md
├── chroma_db/
├── data/
└── screenshots/