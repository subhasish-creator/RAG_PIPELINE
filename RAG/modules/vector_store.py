# Auto-generated: RAG/modules/vector_store.py
import faiss
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex

def create_faiss_index(documents, dim=1536):
    faiss_index = faiss.IndexFlatL2(dim)
    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    return VectorStoreIndex.from_documents(documents, storage_context=storage_context)
