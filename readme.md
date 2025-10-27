# Bindings of Distillation - RAG API

A **Retrieval-Augmented Generation (RAG)** pipeline built with **FastAPI**, **LangChain**, and **Hugging Face Transformers**.  
This app allows you to upload PDF documents, extract and embed their text, and query them using a local language model — creating a mini AI assistant that can answer questions from your own data.

---

## Features

- 🧩 **PDF ingestion** with `PyMuPDF` and text chunking  
- 🔍 **Vector search** powered by `Chroma` and `sentence-transformers`  
- 🤖 **Question answering** using Hugging Face models (`Flan-T5`)  
- ⚡ **FastAPI** backend with `/ask` and `/health` endpoints  
- 📄 Optional **file upload support**  
- 🔁 Real-time latency tracking and structured JSON responses  

---

## Project Structure
bindings-of-distillation-rag/
│
├── main.py # FastAPI app (API routes: /ask, /health)
├── rag.py # Core RAG pipeline (LLM, embeddings, vectorstore)
├── requirements.txt # Python dependencies
├── deploy.sh # Optional Linux/macOS deploy script
├── uploaded_files/ # Folder where uploaded PDFs are stored
└── venv/ # Virtual environment (local setup)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/habdelhadi08/bindings-of-distillation-rag.git
cd bindings-of-distillation-rag
```
### Create and activate a virtual environment

```bash
python -m venv venv
```
### Activate it:
### On Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```
### On macOS/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Running the App
Start the FastAPI app:

```bash
uvicorn main:app --reload
```
## Then open your browser and visit:
http://127.0.0.1:8000/docs

This opens the Swagger UI where you can:

Test /health → returns { "status": "ok" }

Test /ask → upload a PDF and send a JSON question:
{
  "question": "What is data science?"
}

---

## Tech Stack

- FastAPI — high-performance backend

- LangChain — RAG orchestration

- Hugging Face Transformers — LLMs and pipelines

- ChromaDB / FAISS — vector storage

- PyMuPDF — PDF parsing

- Uvicorn — ASGI server

---

## For Windows (manual steps):

```bash

venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
---

## Author

Heba Abdelhadi

Data Scientist & Software Engineer

habdelhadi08@gmail.com

Shelby Township, MI

---


