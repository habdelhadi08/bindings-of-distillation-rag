from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
import time
import fitz  # PyMuPDF
from rag import rag_pipeline  

app = FastAPI(title="Bindings of Distillation - RAG API")

# Health check
@app.get("/health")
def health():
    """Health check endpoint."""
    return "Welcome to the Bindings of Distillation RAG API!"

# Ask endpoint
@app.post("/ask")
async def ask(question: str = Form(...), pdf: UploadFile = File(None)):
    """
    Ask a question about an uploaded PDF.
    If no PDF is provided, the model uses previously loaded data.
    """
    start_time = time.time()
    try:
        if not question.strip():
            raise HTTPException(status_code=400, detail="Empty question.")

        # If a PDF file is provided, extract text and load it into RAG
        if pdf:
            if pdf.content_type != "application/pdf":
                raise HTTPException(status_code=400, detail="Only PDF files are supported.")
       
            pdf_text = ""
            with fitz.open(stream=await pdf.read(), filetype="pdf") as doc:
                for page in doc:
                    pdf_text += page.get_text("text")

            rag_pipeline.load_documents(pdf_text)

        # Ask the model
        answer = rag_pipeline.ask(question)
        sources = ["retrieved_context_1", "retrieved_context_2"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

    latency = round(time.time() - start_time, 3)

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "latency_sec": latency
    }
