from fastapi import FastAPI
from pydantic import BaseModel
from rag import ask_question

app = FastAPI(
    title="Medical RAG Assistant",
    description="Medical Question Answering using RAG",
    version="1.0.0"
)

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {
        "message": "Medical RAG Assistant is running"
    }

@app.post("/ask")
def ask(query: Query):

    answer = ask_question(query.question)

    return {
        "question": query.question,
        "answer": answer
    }
