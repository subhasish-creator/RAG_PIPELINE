import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,StorageContext, load_index_from_storage
from llama_index.core.response.pprint_utils  import pprint_response
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

path='D:\chatbot\data'


# file loading
def loadData(path):
    docs=SimpleDirectoryReader('D:\chatbot\data').load_data()
    return docs

docs1=loadData(path)

index=VectorStoreIndex.from_documents(docs1, show_progress=True)
query_engine=index.as_query_engine()

PERSIST_DIR="D:\chatbot\storage"

path='D:\chatbot\data'
if not os.path.exists(PERSIST_DIR):
    documents=SimpleDirectoryReader(path).load_data()
    index=VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    storage=StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index=load_index_from_storage(storage)


# Loadig the storage from disk
storage_context=StorageContext.from_defaults(persist_dir=PERSIST_DIR)
index2=VectorStoreIndex.load_from_storage(storage_context)
query_engine_new=index2.as_query_engine()
response_new=query_engine_new.query('what causes Global warming')