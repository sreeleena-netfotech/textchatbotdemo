import os

os.environ['OPENAI_API_KEY'] = "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"

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

docse = SimpleDirectoryReader('./data').load_data()
index = VectorStoreIndex.from_documents(docse)

index.storage_context.persist()
print("Done") 

