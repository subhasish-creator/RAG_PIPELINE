# Auto-generated: RAG/modules/query_engine.py
import os
from llama_index.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def build_query_engine(index, config):
    llm = OpenAI(
        model=config["openai"]["model"],
        temperature=config["openai"]["temperature"],
        api_key=os.getenv("OPENAI_API_KEY")
    )
    retriever = index.as_retriever(similarity_top_k=config["retriever"]["similarity_top_k"])
    return index.as_query_engine(retriever=retriever, llm=llm)
