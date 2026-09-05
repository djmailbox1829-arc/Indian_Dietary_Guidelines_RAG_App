# 📚 LangChain + OpenAI + FAISS RAG Application

A simple Retrieval-Augmented Generation (RAG) application built using **LangChain**, **OpenAI**, and **FAISS**.

The application loads information from a PDF document, converts the document into vector embeddings using OpenAI, stores those embeddings in a **local FAISS vector database**, and retrieves the most relevant content when the user asks a question.

The retrieved content is then provided to an OpenAI language model to generate an answer based only on the information available in the document.

---

## 🚀 Features

- 📄 Load PDF documents using LangChain
- ✂️ Split documents into smaller chunks
- 🔢 Generate vector embeddings using OpenAI
- 🗄️ Store vectors in a local FAISS vector database
- 🔎 Perform similarity search to retrieve relevant document chunks
- 🤖 Generate answers using OpenAI GPT
- 🖥️ Simple Streamlit user interface
- 📌 Display the retrieved document chunks along with the answer
- 🔐 API key is stored locally in `.env` and is not included in the repository

---

## 🏗️ Architecture

```text
                PDF Document
                     │
                     ▼
              PyPDFLoader
                     │
                     ▼
          Text Chunking
                     │
                     ▼
          OpenAI Embeddings
          text-embedding-3-small
                     │
                     ▼
              Local FAISS
             Vector Database
                     │
                     │
              User Question
                     │
                     ▼
          OpenAI Embedding
                     │
                     ▼
          FAISS Similarity Search
                     │
                     ▼
          Top Relevant Chunks
                     │
                     ▼
             GPT-4o-mini
                     │
                     ▼
                 Answer
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| LangChain | RAG application framework |
| PyPDF | PDF document loading |
| OpenAI Embeddings | Convert text into vector embeddings |
| FAISS | Local vector database |
| OpenAI GPT-4o-mini | Generate answers |
| Streamlit | Web interface |
| python-dotenv | Load environment variables |

---

## 📁 Project Structure

```text
RAG_APP_D4/
│
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
│
└── data/
    └── RAG_Day4_Project_Data.pdf
```

### Generated locally

When `ingest.py` is executed, the following directory is created:

```text
faiss_db/
├── index.faiss
└── index.pkl
```

The FAISS database is generated locally and does not need to be committed to GitHub.

---

## 📄 Source Document

The application uses:

```text
data/RAG_Day4_Project_Data.pdf
```

This PDF is processed during the ingestion process.

---

## ⚙️ Prerequisites

Make sure you have:

- Python 3.11 or later
- An OpenAI API key
- Internet connection for OpenAI API calls

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd RAG_APP_D4
```

---

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

---

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 🔑 Configure OpenAI API Key

Create a `.env` file in the project root:

```text
RAG_APP_D4/
│
├── .env
├── app.py
├── ingest.py
└── requirements.txt
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

### ⚠️ Important

Do not commit the `.env` file to GitHub.

The API key is a secret and should never be exposed publicly.

---

## 🗄️ Create the FAISS Vector Database

Before running the application for the first time, run:

```powershell
python ingest.py
```

The ingestion process performs the following steps:

1. Loads the PDF.
2. Splits the document into chunks.
3. Creates OpenAI embeddings.
4. Creates a FAISS vector database.
5. Saves the FAISS database locally.

The generated database will be stored in:

```text
faiss_db/
```

---

## ▶️ Run the Application

Start the Streamlit application:

```powershell
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 💬 Example Usage

Enter a question related to the PDF in the Streamlit application.

For example:

```text
What is RAG?
```

The application performs the following:

```text
Question
   ↓
OpenAI Embedding
   ↓
FAISS Similarity Search
   ↓
Retrieve Top 4 Relevant Chunks
   ↓
Send Context + Question to GPT-4o-mini
   ↓
Generate Answer
```

The application also displays the retrieved document chunks so that you can see the information used to generate the answer.

---

## 🔍 Retrieval Configuration

The application retrieves the top 4 most relevant chunks from FAISS.

This is configured in `app.py`:

```python
TOP_K = 4
```

The document chunking configuration is defined in `ingest.py`:

```python
chunk_size=1000
chunk_overlap=150
```

These values can be adjusted depending on the document and retrieval requirements.

---

## 🧠 RAG Workflow

### Step 1 — Document Loading

The PDF is loaded using:

```python
PyPDFLoader
```

### Step 2 — Document Splitting

The document is divided into smaller chunks using:

```python
RecursiveCharacterTextSplitter
```

### Step 3 — Embedding Generation

Each chunk is converted into a vector using:

```text
text-embedding-3-small
```

### Step 4 — Vector Storage

The vectors are stored in:

```text
FAISS
```

The FAISS database is stored locally on the user's machine.

### Step 5 — Retrieval

When a user asks a question, the question is converted into an embedding and FAISS performs similarity search.

The most relevant chunks are retrieved.

### Step 6 — Generation

The retrieved chunks and the user's question are sent to:

```text
GPT-4o-mini
```

The model generates the final answer using the retrieved document context.

---

## 🔐 Data and Security

This project uses:

- **Local FAISS** for vector storage.
- **OpenAI API** for embeddings and answer generation.

The following should remain local:

```text
.env
faiss_db/
venv/
```

Never expose your OpenAI API key in source code or GitHub.

If an API key is accidentally exposed, revoke it and generate a new one.

---

## 🔄 Updating the Document

If the PDF is changed or replaced:

1. Replace the PDF inside:

```text
data/
```

2. Run:

```powershell
python ingest.py
```

The existing FAISS database will be rebuilt using the updated PDF.

3. Start Streamlit:

```powershell
streamlit run app.py
```

---

## 📦 Requirements

The main dependencies are listed in:

```text
requirements.txt
```

Install them using:

```powershell
pip install -r requirements.txt
```

---

## 🧪 Project Workflow

The complete workflow is:

```text
Clone Repository
       ↓
Create Virtual Environment
       ↓
Install Requirements
       ↓
Configure OpenAI API Key
       ↓
Run ingest.py
       ↓
Create Local FAISS Database
       ↓
Run Streamlit
       ↓
Ask Questions
       ↓
Retrieve Relevant Chunks
       ↓
Generate Answer
```

---

## 📌 Important Notes

- FAISS is used as the local vector database.
- OpenAI is used for embeddings and LLM responses.
- The FAISS database must be generated before starting the application for the first time.
- If the source PDF changes, run `python ingest.py` again.
- Do not commit API keys or other secrets to GitHub.

---

## 👨‍💻 Author

**Dinesh Jayaraman**

---

## 📄 License

This project is intended for learning and demonstration purposes.
