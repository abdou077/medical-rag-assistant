# Medical RAG Assistant

Medical RAG Assistant is a Retrieval-Augmented Generation (RAG) application designed to answer medical questions using indexed medical documents.

The system combines semantic search with a Large Language Model (LLM) to generate contextualized and evidence-based answers from a medical knowledge base.

---

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic Search using ChromaDB
* OpenAI GPT Integration
* FastAPI REST API
* Dockerized Deployment
* Medical Document Indexing
* Context-Aware Question Answering

---

## Tech Stack

### Generative AI

* OpenAI API
* LangChain
* Retrieval-Augmented Generation (RAG)

### Vector Database

* ChromaDB
* OpenAI Embeddings

### Backend

* FastAPI
* Python

### Deployment

* Docker

---

## Project Architecture

```text
User Question
      |
      v
ChromaDB Semantic Search
      |
      v
Relevant Medical Context
      |
      v
OpenAI GPT Model
      |
      v
Contextualized Answer
```

---

## Example Question

```text
What are the main risk factors for Type 2 Diabetes?
```

## Example Response

```text
According to the indexed medical guidelines, major risk factors include obesity, physical inactivity, hypertension, family history, age over 45 years, and unhealthy dietary habits.
```

---

## Project Structure

```text
medical-rag-assistant/

├── app/
│   ├── main.py
│   ├── rag.py
│   └── index_documents.py
│
├── data/
│   └── medical_documents.pdf
│
├── chroma_db/
│
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/abdou077/medical-rag-assistant.git
cd medical-rag-assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Index Medical Documents

Place your medical PDF documents inside the `data/` directory.

Run:

```bash
python app/index_documents.py
```

This step generates vector embeddings and stores them in ChromaDB.

---

## Run the API

```bash
uvicorn app.main:app --reload
```

API documentation will be available at:

```text
http://localhost:8000/docs
```

---

## API Endpoint

### Ask a Medical Question

**POST**

```text
/ask
```

Request Body:

```json
{
  "question": "What are the symptoms of hypertension?"
}
```

Response:

```json
{
  "question": "What are the symptoms of hypertension?",
  "answer": "Hypertension is often asymptomatic, but may be associated with headaches, dizziness and cardiovascular complications."
}
```

---

## Future Improvements

* Multi-document retrieval
* Medical guideline ingestion pipeline
* Authentication and user management
* Frontend interface with Streamlit
* AWS deployment
* Conversation memory
* Support for local LLMs (Llama)

---

## Author

Abdelghafour Nachidi

AI Engineer | Data Scientist

Paris, France
