# RAG_pipeline

RAG
AI Assistant Powered by RAG (Retrieval-Augmented Generation)
This is a simple AI assistant built using Streamlit and LlamaIndex, that allows users to upload context files (PDF/TXT) and ask questions based on their content using OpenAI GPT models.

Features
Upload PDF or TXT documents
Index content using FAISS + LlamaIndex
Ask context-aware questions
Powered by OpenAI GPT (e.g., gpt-3.5-turbo)
Lightweight, fast, and easy to use via a web UI
Technologies Used
Python 🐍
Streamlit
FAISS
LlamaIndex
OpenAI API
Setup Instructions
Clone the repo
git clone https://github.com/subhasish-creator/RAG.git
cd your-repo-name

streamlit run app_rag.py --server.address 127.0.0.1 --server.port 8502

## Folder Struccture Information:
- RAG folder consist components, config,data,modules and utils blocks
- data folder hold the supplied data file (PDF or Txt)
- config folder hold config.yaml file. This file talk about LLM model name and its parameter.
- modules\config_loader.py load the LLM model as perconfiguration of yaml file
- modules\data_loader.py load the data file needed for embedding
- modules\vectore_store.py is use for VectorDB creation
- modules\query_engine.py is use for handling query
- modules\task2.py is use for storing Database locally
- Storage folder store knowledgeDB created by VectorStorIndex locally in HardDisk
- app.py for UI part of LLM
  
