
# RAG Project

## Overview
The RAG Project is a web application designed for managing and interacting with text documents. This project leverages **LangChain** for document processing, **Ollama** for embeddings, and **FastAPI** for creating a robust API backend. The application allows users to query the documents and retrieve relevant answers based on the content.

## Features
- **Document Upload**: Supports uploading and processing both text files and PDF files from specified folders.
- **Text Splitting**: Uses LangChain's `RecursiveCharacterTextSplitter` to break large text documents into smaller chunks.
- **PDF Text Extraction**: Extracts text from PDF files using **PyMuPDF** (fitz), making PDF content searchable and retrievable.
- **Vectorization**: Embeds text data into vector representations using the **Ollama** embeddings model.
- **QA System**: Built with LangChain's `RetrievalQA`, it allows users to ask questions and retrieve answers from the document corpus.
- **FastAPI Backend**: Provides a RESTful API to interact with the document corpus and the query system.

## Installation  

1. **Clone the repository:**
```bash  
git clone https://github.com/JowanaA/RAG_Project.git  
cd RAG_Project
```

2. ***Create and activate a virtual environment***
```bash
python -m venv .venv  
source .venv/bin/activate    # On Windows use `.venv\Scripts\activate`
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
uvicorn main:app --reload
```
5. **Access the API Documentation: Once the application is running, you can access the FastAPI interactive documentation by navigating to:**
```bash 
http://127.0.0.1:8000/docs
```
This will display an interactive interface where you can explore and test the API endpoints.




## Usage

1. **Upload Text Files**: Add your text files in the `txtMap` folder.
2. **Upload PDF Files**: Add your PDF files in the pdfMap folder. The system will automatically extract text from these PDFs and include them in the document corpus.
3. **Query the Documents**: You can query the system through the FastAPI backend. The system will search through the documents (both text and PDF) and return relevant answers.

## Technologies Used
- **Python**: Programming language used for the project.
- **FastAPI**: Framework used for building the API backend.
- **LangChain**: Library used for text processing and document querying.
- **Ollama**: Provides embeddings for text documents.
- **PyMuPDF (fitz)**: Used for extracting text from PDF documents to be processed and queried.

