# 🧠 Medical RAG Bot

A Retrieval-Augmented Generation (RAG) AI assistant for answering medical questions using authoritative guidelines (WHO, CDC, India Dengue Guidelines). Built with FastAPI (backend), Streamlit (frontend), and local LLMs for privacy and performance.

---

## 🚀 Features
- **Ask medical questions** and get answers with source references
- Uses local PDF guidelines as knowledge base
- FastAPI backend with RAG pipeline (vector search + LLM)
- Streamlit web UI for easy interaction
- Cites sources for transparency
- Runs fully locally (no data leaves your machine)

---

## 🏗️ Project Structure
```
medical_rag_bot/
├── frontend/         # Streamlit web app
│   └── app.py
├── src/              # Backend (FastAPI + RAG logic)
│   ├── main.py
│   ├── query.py
│   └── ingest.py
├── data/             # PDF guideline documents (ignored by git)
├── vectorstore/      # FAISS vector index (ignored by git)
├── models/           # LLM binaries (ignored by git)
├── venv/             # Python virtual environment (ignored by git)
└── .gitignore
```

---

## ⚡ Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/dariyaDeepanshu/medical_rag_bot.git
cd medical_rag_bot
```

### 2. Install dependencies
Create and activate a virtual environment, then install requirements (see below for example):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Prepare data and models
- Place your PDF guidelines in the `data/` folder.
- Download or place your LLM model files in `models/` (these are **not** included in the repo).

### 4. Ingest documents
```bash
python src/ingest.py
```
This will create a FAISS vector index in `vectorstore/`.

### 5. Start the backend API
```bash
uvicorn src.main:app --reload
```

### 6. Launch the frontend
```bash
streamlit run frontend/app.py
```

---

## 🧩 How it Works
- **Ingestion:** `src/ingest.py` loads PDFs, chunks text, generates embeddings, and builds a FAISS vectorstore.
- **Backend:** `src/main.py` loads the vectorstore and a local LLM, exposes a `/query` endpoint for Q&A.
- **Frontend:** `frontend/app.py` provides a chat UI, sending questions to the backend and displaying answers with sources.

---

## 📁 Data & Models
- **PDFs:** Place in `data/` (not tracked by git)
- **Vectorstore:** Auto-generated in `vectorstore/` (not tracked by git)
- **Models:** Place LLM binaries in `models/` (not tracked by git)

> **Note:** Large model files and data are excluded from the repository via `.gitignore`.

---

## 🛠️ Requirements
- Python 3.8+
- FastAPI
- Streamlit
- langchain
- sentence-transformers
- ctransformers
- faiss-cpu
- requests

*(Add a `requirements.txt` with these packages for easy setup)*

---

## 🤝 Contributing
Pull requests and issues are welcome!

---

## 📜 License
MIT License 