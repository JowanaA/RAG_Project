# RAG Project

## Overview
The RAG Project is a web application designed for managing and interacting with text documents. This project leverages **LangChain** for document processing, **Ollama** for embeddings, and **FastAPI** for creating a robust API backend. The application allows users to query the documents and retrieve relevant answers based on the content.

## Features
- **Document Upload**: Supports uploading and processing text files from a specified folder.
- **Text Splitting**: Uses LangChain's `RecursiveCharacterTextSplitter` to break large text documents into smaller chunks.
- **Vectorization**: Embeds text data into vector representations using the **Ollama** embeddings model.
- **QA System**: Built with LangChain's `RetrievalQA`, it allows users to ask questions and retrieve answers from the document corpus.
- **FastAPI Backend**: Provides a RESTful API to interact with the document corpus and the query system.

