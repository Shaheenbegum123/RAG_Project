# AI Based Document Search and Knowledge Retrieval with Conversational Interface

---

## Overview

This project is a Retrieval Augmented Generation (RAG) system that allows users to ask questions from multiple PDF books and get answers in main points.

The system uses:

- Python  
- LangChain  
- HuggingFace Embeddings  
- Chroma Vector Database  
- Sentence Transformers  

---

## Project Folder Structure


AI_Document_Search_Project/
│
├── Main.py
├── requirements.txt
├── README.md
├── Books/
│ ├── Building Machine Learning Systems with Python.pdf
│ ├── Introduction to Machine Learning with Python.pdf
│ ├── Practical Machine Learning with Python.pdf
│
├── venv/
├── chroma_db/


---

## Step 1: Clone Repository

Open Command Prompt and run:


git clone https://github.com/YOUR_USERNAME/AI_Document_Search_Project.git

cd AI_Document_Search_Project


---

## Step 2: Create Virtual Environment


python -m venv venv


---

## Step 3: Activate Virtual Environment

Windows:


venv\Scripts\activate


You should see:


(venv)


---

## Step 4: Install Required Libraries


pip install -r requirements.txt


If requirements.txt is not available, install manually:


pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers pypdf


---

## Step 5: Run the Project


python Main.py


---

## Step 6: Ask Questions

Example:


Enter your query: What is machine learning?


Output:


Main Points:

• Machine learning learns from data
• It improves automatically
• Used in AI applications
• Helps in prediction
• Used in real-world systems
• Improves performance with experience
• Works using algorithms
• Used in many industries


---

## Step 7: Exit Program

Type:


exit


---

## First Run Note

First time running may take few minutes because:

- Embedding model downloads  
- Chroma database creates  

After first run, execution becomes fast.

---

## Create requirements.txt (if not present)

Run:


pip freeze > requirements.txt


---

## Technologies Used

- Python  
- LangChain  
- HuggingFace  
- ChromaDB  
- Sentence Transformers  

---

## Features

- Supports multiple PDF documents  
- Fast semantic search using ChromaDB  
- Provides main points as output  
- Interactive query interface  
- Persistent vector database  
- Duplicate result filtering  
- Fast retrieval after first run  

---

## Author

Name: Shaheen Begum  
Project: Infosys Springboard Project
