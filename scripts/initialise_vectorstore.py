from pathlib import Path

from src.rag.ingest import create_vectorstore

folder = Path("chroma_db")

if folder.is_dir():
    print("Vectorstore already exists")
else:
    create_vectorstore()