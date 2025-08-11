from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Adaptive RAG - Programming Education")

class CodeQuery(BaseModel):
    user_id: str
    prompt: str
    language: str = "python"

@app.post("/query")
async def query_code(query: CodeQuery):
    # Placeholder: call retriever + generator + adaptive policy
    return {
        "user_id": query.user_id,
        "prompt": query.prompt,
        "language": query.language,
        "answer": "This is a placeholder response. Replace with RAG pipeline."
    }

@app.get("/")
async def root():
    return {"message": "Adaptive RAG API - replace with actual pipeline"}
