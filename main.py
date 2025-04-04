from fastapi import FastAPI
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

app = FastAPI()

embedding_model = OllamaEmbeddings(model="nomic-embed-text")
llm = Ollama(model="gemma2:9b")


text_folder = "./txtMap"  # min text folder
all_documents = []

for filename in os.listdir(text_folder): #får alle filer fra mappen
    if filename.endswith(".txt"):  # sikre at den læser kun txt filer
        file_path = os.path.join(text_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            all_documents.append(Document(page_content=text, metadata={"source": filename})) #læser alle filer og gemmer den i all_documents

#opdele teksten i mindre dele
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(all_documents)

#lav teksten om til vector og gemme den i FAISS
vector_store = FAISS.from_documents(split_docs, embedding_model)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever())



@app.post("/prompt")
async def prompt(user_query: str):
    response = qa_chain.run(user_query)
    return {"Answer": response}

