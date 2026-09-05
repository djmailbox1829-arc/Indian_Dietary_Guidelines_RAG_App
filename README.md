# Local LangChain RAG App — FAISS + OpenAI

This project converts the supplied PDF into a simple RAG application.

## Architecture

PDF
→ PyPDFLoader
→ Text Splitter
→ Local Hugging Face Embeddings
→ Local FAISS Vector DB
→ User Question
→ Similarity Search
→ OpenAI GPT-4o-mini
→ Answer

The vector database is completely local and is saved in the `faiss_db` folder.

## 1. Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Install packages

```bash
pip install -r requirements.txt
```

## 3. Add your OpenAI API key

Copy `.env.example` to `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Do not commit `.env` to Git.

## 4. Create the local FAISS vector database

Run:

```bash
python ingest.py
```

This will:

1. Load the supplied PDF.
2. Split it into chunks.
3. Create embeddings locally.
4. Build a FAISS index locally.
5. Save the index in `faiss_db/`.

## 5. Start the application

```bash
streamlit run app.py
```

## Example questions

- What is a balanced diet?
- What foods are included in the 10 food groups?
- What does the document recommend for a 2000 Kcal diet?
- What are the recommendations for sugar intake?
- What are the protein sources mentioned in the document?

## Components

- **Document:** Supplied PDF
- **PDF loader:** PyPDFLoader
- **Text splitter:** RecursiveCharacterTextSplitter
- **Embeddings:** sentence-transformers/all-MiniLM-L6-v2
- **Vector DB:** FAISS (local)
- **LLM:** OpenAI GPT-4o-mini
- **UI:** Streamlit

No Ollama or Chroma is required.
