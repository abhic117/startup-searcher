from src.rag.ingest import get_vectorstore

def retrieve(query):
    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in results])