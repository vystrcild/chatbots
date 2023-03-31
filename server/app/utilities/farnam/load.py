from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import os
from dotenv import load_dotenv

load_dotenv()

# Loading files
loader = DirectoryLoader("parsed", glob="*.txt", loader_cls=TextLoader)
docs = loader.load()


# Chunk data up into smaller documents
splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1000,
    chunk_overlap  = 200,
)
docs = splitter.split_documents(docs)

# Create embeddings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

docsearch = Chroma.from_documents(docs, embeddings, persist_directory="db")