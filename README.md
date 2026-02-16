# AI Based Document Search and Knowledge Retrieval with Conversational Interface 

## Overview

This project is a Retrieval Augmented Generation (RAG) system that allows users to ask questions from multiple PDF books and get answers in main points.

The system uses:

Python
LangChain
HuggingFace Embeddings
FAISS Vector Database
Sentence Transformers

---

## Project Folder Structure

```
AI_Document_Search_Project/
│
├── Main.py
├── requirements.txt
├── README.md
├── Books/
│   ├── Building Machine Learning Systems with Python.pdf
│   ├── Introduction to Machine Learning with Python.pdf
│   ├── Practical Machine Learning with Python.pdf
│
├── venv/
├── faiss_index/
```

---

## Step 1: Clone Repository

Open Command Prompt and run:

```
git clone https://github.com/YOUR_USERNAME/AI_Document_Search_Project.git
cd AI_Document_Search_Project
```

---

## Step 2: Create Virtual Environment

```
python -m venv venv
```

---

## Step 3: Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

You should see:

```
(venv)
```

---

## Step 4: Install Required Libraries

```
pip install -r requirements.txt
```

If FAISS gives error, install manually:

```
pip install faiss-cpu
```

---

## Step 5: Run the Project

```
python Main.py
```

---

## Step 6: Ask Questions

Example:

```
Enter your query: What is machine learning?
```

Output:

```
Main Points:

• Machine learning learns from data  
• It improves automatically  
• Used in AI applications  
• Helps in prediction  
• Used in real-world systems  
• Improves performance with experience  
• Works using algorithms  
• Used in many industries  
```

---

## Step 7: Exit Program

Type:

```
exit
```

---

## First Run Note

First time running may take few minutes because:

Embedding model downloads
FAISS index creates

After first run, execution becomes fast.

---

## Install Requirements File (if not present)

Run this command to create requirements.txt:

```
pip freeze > requirements.txt
```

---

## Technologies Used

Python
LangChain
HuggingFace
FAISS
Sentence Transformers

---

## Features

Supports multiple PDFs

Fast FAISS search

Main points output

Interactive query system

---

## Author

Name: Shaheen Begum

Project: Infosys Springboard Project
