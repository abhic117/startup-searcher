from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

from src.database import get_startups

def create_vectorstore():
    # Get all startups from database
    startups = get_startups()
    startups = startups[:20]

    # Write startups to  text file
    with open("data/startups_text.txt", "w", encoding="utf-8") as file:
        for startup in startups:
            file.write(startup.toString() + "\n")

    # Load text document
    docs = TextLoader("data/startups_text.txt", encoding="utf-8").load()

    # Split document into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=1500)
    chunks = splitter.split_documents(docs)

    # Embed chunks (convert to vectors) and store them in vector database
    embeddings = OllamaEmbeddings(model="qwen2.5:7b-instruct-q4_K_M")
    vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="chroma_db")

def get_vectorstore():
    embeddings = OllamaEmbeddings(model="qwen2.5:7b-instruct-q4_K_M")
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    return vectorstore