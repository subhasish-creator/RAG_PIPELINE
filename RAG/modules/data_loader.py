# Auto-generated: RAG/modules/data_loader.py
from llama_index.core import SimpleDirectoryReader

def load_documents(input_dir: str):
    return SimpleDirectoryReader(input_dir).load_data()
