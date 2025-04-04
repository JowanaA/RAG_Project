from fastapi import FastAPI
import os
import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

app = FastAPI()

embedding_model = OllamaEmbeddings(model="nomic-embed-text")
llm = Ollama(model="gemma2:9b")


text_folder = "./txtMap"
pdf_folder = "./pdfMap"
all_documents = []


# Function to extract text from PDF using PyMuPDF (fitz)
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n" # Extract text from each page and add it to the string
    return text



# Loop through all files in the text folder and read .txt files
for filename in os.listdir(text_folder): # Get all files in the text folder
    if filename.endswith(".txt"):   # Ensure only .txt files are processed
        file_path = os.path.join(text_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            all_documents.append(Document(page_content=text, metadata={"source": filename})) #læser alle filer og gemmer den i all_documents


for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):  # Ensure only pdf files are processed
        pdf_path = os.path.join(pdf_folder, filename)
        try:
            pdf_text = extract_text_from_pdf(pdf_path)
            all_documents.append(Document(page_content=pdf_text, metadata={"source": filename}))  # Add each PDF content as a Document
        except Exception as e:
            print(f"Error reading PDF {filename}: {e}")

# Split the collected documents into smaller chunks for processing
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(all_documents)

# Convert the documents into vectors and store them in FAISS for efficient similarity search
vector_store = FAISS.from_documents(split_docs, embedding_model)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever())



@app.post("/prompt")
async def prompt(user_query: str):
    response = qa_chain.run(user_query)
    return {"Answer": response}

