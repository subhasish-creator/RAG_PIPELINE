# Auto-generated: app.py

import os
import streamlit as st
import faiss
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,StorageContext, load_index_from_storage
from llama_index.core.response.pprint_utils  import pprint_response
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import tempfile
import shutil


load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

st.set_page_config(page_title="AI Assistant powered by RAG", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Upload the Context and Ask Anything relevant to Context')

# File Uplader

file_upload=st.file_uploader('Upload pdf or text file', type=["pdf", "txt"])
if file_upload:
    with tempfile.TemporaryDirectory() as filedir:
        file_path=os.path.join(filedir,file_upload.name)
        with open(file_path ,"wb") as f:
            f.write(file_upload.read())

        documents=SimpleDirectoryReader(filedir).load_data()
        faiss_index=faiss.IndexFlatL2(1536)
        vector_store=FaissVectorStore(faiss_index=faiss_index)
        storage_context=StorageContext.from_defaults(vector_store=vector_store)

        index=VectorStoreIndex.from_documents(documents,storage_context=storage_context)

        
        llm=OpenAI(model='gpt-3.5-turbo', temperature=0.2)
        retriver=index.as_retriever(similarity_top_k=3)
        query_engine=index.as_query_engine(retriver=retriver, llm=llm)

        st.subheader("Ask Any question based on Context")
        user_query=st.text_input("Write your Question here")

        if user_query:
            with st.spinner('Analysing.......'):
                response=query_engine.query(user_query)
                st.success("Answer :")
                st.write(response.response)
