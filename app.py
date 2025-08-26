import streamlit as st
from langchain_groq import ChatGroq
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Page Config ---
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 Webpage Q&A Chatbot")
st.write("Ask questions based on the content of a webpage!")

# --- Sidebar Config ---
st.sidebar.header("Settings")
url = st.sidebar.text_input("Enter webpage URL:",
                            value="https://python.langchain.com/docs/integrations/tools/")

if st.sidebar.button("Load Webpage"):
    with st.spinner("🔎 Loading and processing webpage..."):
        # Load documents
        loader = WebBaseLoader(url)
        documents = loader.load()

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        docs = splitter.split_documents(documents)

        # Initialize embeddings
        os.environ["TRANSFORMERS_NO_TF"] = "1"   # Disable TensorFlow usage in HuggingFace
        embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

        # Create FAISS vector DB
        vector_store = FAISS.from_documents(docs, embedding=embeddings)

        # Save to session state
        st.session_state.retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 3, "lambda_mult": 0.5}
        )
        st.success("✅ Webpage loaded and indexed!")


# --- Initialize Model ---
if "model" not in st.session_state:
    st.session_state.model = ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.5,
        max_tokens=512,
    )

# --- Prompt Template ---
qa_prompt = PromptTemplate(
    template="""
You are a helpful assistant that answers questions based on a webpage.

Conversation so far:
{history}

Here is the webpage text (retrieved context):
----------------
{context}
----------------

Now, using ONLY the webpage text above:
Q: {question}
A:""",
    input_variables=["history", "context", "question"]
)

# --- Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Chat Input ---
query = st.chat_input("Ask a question about the webpage...", key="chat_input")

if query:
    if query.lower() == "exit":
        st.write("Thank you, see you soon 👋")
        st.stop()

    if "retriever" in st.session_state:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": query})

        # Build history context
        history_context = "\n".join(
            [f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages]
        )

        # Retrieve relevant docs
        results = st.session_state.retriever.invoke(query)
        docs_context = "\n".join([doc.page_content for doc in results])

        # Format prompt
        formatted_prompt = qa_prompt.format(
            history=history_context,
            context=docs_context if docs_context.strip() else "No relevant text found.",
            question=query
        )

        # Call LLM
        ans = st.session_state.model.invoke(formatted_prompt)
        response = ans.content

        # Append AI response
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.info("Please load a webpage first from the sidebar.")

# --- Display Chat ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# '''
# Since my working directory different from the venv directory so
# To run the scripts run this in terminal ""c:\DATA SCIENCE\GEN AI\LangChain\Langchain Models\venv\Scripts\python.exe" -m  streamlit run app.py"
# '''
