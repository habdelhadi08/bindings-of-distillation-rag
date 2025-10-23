from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time

app = FastAPI()

# Define a request schema
class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/ask")
def ask(request: QuestionRequest):
    """Ask endpoint for RAG pipeline."""
    start_time = time.time()

    try:
        # 🔹 Replace with your actual RAG logic later
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Empty question.")
        
        answer = f"Simulated RAG answer for: {request.question}"
        sources = ["chunk_1", "chunk_2"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    latency = round(time.time() - start_time, 3)

    return {
        "answer": answer,
        "sources": sources,
        "latency_sec": latency
    }
