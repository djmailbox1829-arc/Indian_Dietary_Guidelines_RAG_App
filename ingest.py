from pathlib import Path
import shutil

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


# Load environment variables
load_dotenv()


# Project directories
BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR / "data" / "RAG_Day4_Project_Data.pdf"
DB_DIR = BASE_DIR / "faiss_db"


def main():
    print("Starting document ingestion...")

    # Check PDF
    if not PDF_PATH.exists():
        raise FileNotFoundError(
            f"PDF not found: {PDF_PATH}"
        )

    # Remove old FAISS database
    if DB_DIR.exists():
        print("Removing old FAISS database...")
        shutil.rmtree(DB_DIR)

    # Load PDF
    print("Loading PDF...")
    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    print(f"Loaded {len(documents)} pages.")

    # Split documents into chunks
    print("Splitting document into chunks...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # OpenAI Embeddings
    print("Creating OpenAI embeddings...")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # Create FAISS vector database
    print("Creating FAISS vector database...")

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    # Save FAISS locally
    vector_db.save_local(str(DB_DIR))

    print()
    print("====================================")
    print("FAISS database created successfully!")
    print(f"Location: {DB_DIR}")
    print(f"Total chunks: {len(chunks)}")
    print("====================================")


if __name__ == "__main__":
    main()