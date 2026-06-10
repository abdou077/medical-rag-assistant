Medical RAG Assistant

Medical RAG Assistant is a Retrieval-Augmented Generation (RAG) application designed to answer medical questions using indexed medical documents.

Features

- Retrieval-Augmented Generation (RAG)
- Semantic Search with ChromaDB
- OpenAI GPT Integration
- FastAPI REST API
- Docker Deployment
- Medical Document Retrieval

Tech Stack

- Python
- LangChain
- OpenAI API
- ChromaDB
- FastAPI
- Docker

Architecture

User Question → ChromaDB Retrieval → Relevant Medical Context → OpenAI LLM → Contextualized Answer

Example Question

What are the major risk factors for Type 2 Diabetes?

Example Response

According to the indexed clinical guidelines, major risk factors include obesity, physical inactivity, hypertension, family history, and age over 45 years.

Future Improvements

- Multi-document retrieval
- Medical PDF ingestion pipeline
- Authentication
* Streamlit frontend
* Deployment on AWS
