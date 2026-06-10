import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

embedding_model = OpenAIEmbeddings()

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

def ask_question(question: str):

    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    You are a medical assistant.

    Answer ONLY using the information provided.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content
