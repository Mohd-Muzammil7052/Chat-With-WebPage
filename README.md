# 🤖 Webpage Q&A Chatbot  

A Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit** and **LangChain**, allowing you to query the contents of any webpage. It loads a webpage, chunks and embeds the text, stores it in a FAISS vector database, and answers your questions using a lightweight Groq-hosted LLM.  

This repository also includes example notebooks demonstrating basic RAG with both **web content** and **Wikipedia**.  

---

## 📑 Table of Contents
- [Introduction](#introduction)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Configuration](#configuration)  
- [Examples](#examples)  
- [Dependencies](#dependencies)  
- [Troubleshooting](#troubleshooting)  
- [Contributors](#contributors)  
- [License](#license)  

---

## 📝 Introduction  

The **Webpage Q&A Chatbot** enables interactive Q&A over any webpage. It uses:  
- **LangChain** for retrieval and prompt orchestration  
- **HuggingFace sentence-transformer embeddings** for semantic search  
- **FAISS** for fast vector storage and retrieval  
- **Groq LLM (llama-3.1-8b-instant)** for generating responses  

You can either:  
1. Run the **Streamlit app** (`app.py`) for a UI-based chatbot experience.  
2. Explore the **Jupyter notebooks** (`basic_web_rag.ipynb`, `basic_wikipedia_rag.ipynb`) for code-based demos of RAG workflows.  

---

## ✨ Features  

- 🌐 Load any webpage and build a local FAISS index  
- 🔎 Ask questions based only on the retrieved webpage text  
- ⚡ Uses small, fast embeddings (`all-MiniLM-L6-v2`) for efficiency  
- 💾 Saves FAISS index locally for re-use  
- 🧠 Lightweight chat history (last 3 messages kept) to reduce memory usage  
- 🖥️ Streamlit web UI for interactive use  

---

## 🚀 Installation  

Clone the repo and install dependencies:  

```bash
git clone <https://github.com/Mohd-Muzammil7052/Chat-With-WebPage.git>
cd <Chat-With-WebPage>
pip install -r requirements.txt

---

## ⚙️ Setup


