import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate


# Load environment variables
load_dotenv()


# Project directory
BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "faiss_db"


# Streamlit page configuration
st.set_page_config(
    page_title="DIETARY GUIDELINES FOR INDIANS",
    page_icon="📚",
    layout="wide"
)


st.title("📚 PDF Question Answering - DIETARY GUIDELINES FOR INDIANS")
st.write(
    "Ask questions about the PDF - DIETARY GUIDELINES FOR INDIANS"
)


# Check API key
if not os.getenv("OPENAI_API_KEY"):
    st.error(
        "OPENAI_API_KEY is not configured. "
        "Please add it to your .env file."
    )
    st.stop()


# Check FAISS database
if not DB_DIR.exists():
    st.error(
        "FAISS database not found.\n\n"
        "Please run `python ingest.py` first."
    )
    st.stop()


# Create OpenAI embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# Load local FAISS database
vector_db = FAISS.load_local(
    str(DB_DIR),
    embeddings,
    allow_dangerous_deserialization=True
)


# OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Number of documents to retrieve
TOP_K = 4


# Prompt
prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant answering questions
about the provided document.

Answer the question using ONLY the information
contained in the context below.

If the answer cannot be found in the context,
respond exactly with:

"I could not find that information in the document, please provide more details to deep search"

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""
)


# User question
question = st.text_input(
    "Ask a question about the PDF:"
)


if question:

    with st.spinner("Searching the document..."):

        # Search FAISS
        retrieved_docs = vector_db.similarity_search(
            question,
            k=TOP_K
        )

        # Build context
        context_parts = []

        for doc in retrieved_docs:

            page_number = doc.metadata.get(
                "page",
                "Unknown"
            )

            context_parts.append(
                f"Page {page_number + 1}:\n"
                f"{doc.page_content}"
            )

        context = "\n\n".join(context_parts)

        # Create prompt
        messages = prompt.format_messages(
            context=context,
            question=question
        )

        # Ask OpenAI
        response = llm.invoke(messages)

    # Display answer
    st.subheader("Answer")

    st.write(response.content)

    # Display retrieved chunks
    with st.expander("🔎 Retrieved document chunks"):

        for i, doc in enumerate(retrieved_docs, start=1):

            page_number = doc.metadata.get(
                "page",
                "Unknown"
            )

            st.markdown(
                f"### Chunk {i} — Page {page_number + 1}"
            )

            st.write(doc.page_content)