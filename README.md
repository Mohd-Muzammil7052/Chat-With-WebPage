# 🤖 Webpage Q&A Chatbot  

A Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit** and **LangChain**, allowing you to query the contents of any webpage. It loads a webpage, chunks and embeds the text, stores it in a FAISS vector database, and answers your questions using a lightweight Groq-hosted LLM.  

This repository also includes example notebooks demonstrating basic RAG with both **web content** and **Wikipedia**.  

---

## 📑 Table of Contents
- [Introduction](#introduction)  
- [Features](#features)  
- [Installation](#installation)
- [Setup](#setup)  
- [Usage](#usage)
- [Jupyter Notebooks](#jupyternotebooks)
- [Tech Stack](#techstack)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [License](#license)    
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgements)
- [Contact](#contact)  


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
git clone https://github.com/Mohd-Muzammil7052/Chat-With-WebPage.git
cd Chat-With-WebPage
pip install -r requirements.txt

```


## ⚙️ Setup

1. Create a .env file in the project root and add your API keys (e.g., Groq API key):

```env
GROQ_API_KEY=your_api_key_here
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the Streamlit app in your browser.
2. Enter any webpage URL in the sidebar.
3. Click "Load Webpage" to process and index the content.
4. Start asking questions about the webpage in the chat input!

---

## 📓 Jupyter Notebooks

- basic_web_rag.ipynb → Shows how to perform RAG over a webpage using LangChain.
+ basic_wikipedia_rag.ipynb → Demonstrates RAG over Wikipedia content.

These notebooks provide a step-by-step breakdown of how RAG works without the Streamlit UI.

---

## 🛠️ Tech Stack

* Streamlit → Web UI for chatbot.
- LangChain → RAG pipeline.
+ Groq LLMs → Fast inference models.
* Hugging Face Transformers → Sentence embeddings.
- FAISS → Vector similarity search.

---

## 📌 Requirements

See [requirements.txt](https://github.com/Mohd-Muzammil7052/Chat-With-WebPage/blob/main/requirements.txt) for all dependencies:

```text
streamlit == 1.48.0
python-dotenv == 1.1.1
langchain == 0.3.27
langchain-community == 0.3.27
langchain-core == 0.3.74
langchain-groq == 0.3.7
langchain-huggingface == 0.3.1
sentence-transformers == 5.1.0
faiss-cpu == 1.12.0
beautifulsoup4 == 4.13.5
lxml == 6.0.1
```

---

## 🏗️ Project Structure  

```text
📦 Chat-With-WebPage
 ┣ 📜 README.md                   # Documentation
 ┣ 📜 app.py                      # Streamlit chatbot app
 ┣ 📜 basic_web_rag.ipynb         # RAG with Webpages (Notebook)
 ┣ 📜 basic_wikipedia_rag.ipynb   # RAG with Wikipedia (Notebook)
 ┣ 📜 requirements.txt            # Project dependencies
 ┗ 📜 .env.example                # Example env file (create your own)
```

---

## 📄 License  

This project is licensed under the [MIT License](https://opensource.org/license/mit).  
Feel free to use, modify, and distribute it as needed.

---

## 🤝 Contributing  

Contributions are welcome! 🎉  
If you’d like to improve this project:  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 🙌 Acknowledgments  

Special thanks to the amazing open-source tools powering this project:  

- [LangChain](https://www.langchain.com/)  
- [Hugging Face](https://huggingface.co/)  
- [Groq](https://groq.com/)  
- [Streamlit](https://streamlit.io/)  

---

## 📧 Contact  

For queries or collaborations:  

**Mohd Muzammil**  
- [GitHub](https://github.com/Mohd-Muzammil7052)  
- [LinkedIn](https://www.linkedin.com/in/mohd-muzammil-109044290/)  





