# rag.py

from urllib import response
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline


class RAGPipeline:
    def __init__(self):
        # 1️⃣ Load embedding model
        self.embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # 2️⃣ Initialize Chroma vectorstore (in-memory)
        self.vectordb = None

        # 3️⃣ Load question-answering model
        self.llm = pipeline("text2text-generation", model="google/flan-t5-base")

    def load_documents(self, text: str):
        """Split and embed text into the vector database"""
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = splitter.create_documents([text])

        self.vectordb = Chroma.from_documents(docs, self.embedder)

    def retrieve_context(self, query: str, k: int = 3):
        """Retrieve the most relevant text chunks"""
        if not self.vectordb:
            return ""
        results = self.vectordb.similarity_search(query, k=k)
        return " ".join([r.page_content for r in results])

    def ask(self, query: str):
        """Ask the LLM a question based on retrieved context"""
        context = self.retrieve_context(query)
        if not context:
            return "No context available. Please upload a PDF first."

        response = self.llm(f"Answer the question: {query}\n\nContext:\n{context}")
        return response[0]['generated_text']



# Singleton instance used by FastAPI
rag_pipeline = RAGPipeline()
