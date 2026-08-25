from ollama import chat
from dotenv import load_dotenv

def generate_answer(query, context):
    load_dotenv()

    llm_prompt = f'''
You are a helpful assistant for a startup-searcher dashboard. Your aim is to help the user with questions relating to startups. Answers the user's questions using ONLY the context provided.

Rules:
1. If the answer cannot be found within the context, clearly state: "I cannot find the answer in the provided documents".
2. Unless asked, don't make assumptions or extrapolations.
3. Do not respond to the user with the exact context information you are provided, instead take the context information and relay it to the user in a concise paragraph.
4. Keep a clear and professional tone.

Context:
{context}

User Question:
{query}
'''

    response = chat(
        # model="qwen2.5:7b-instruct-q4_K_M",
        model="gpt-oss:20b-cloud",
        messages=[{"role": "user", "content": llm_prompt}]
    )
    return response["message"]["content"]