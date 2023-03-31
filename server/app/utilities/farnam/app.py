import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain import VectorDBQA
from langchain.chains.question_answering import load_qa_chain
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def filename_to_url(input_string):
    # Remove the directory and extension from the input_string
    file_name = input_string.split('/')[-1].split('.')[0]

    # Replace spaces with %20 for the URL
    search_query = file_name.replace(" ", "%20")

    # Create the final URL
    url = f"https://fs.blog/?s={search_query}"
    return url

@st.cache_resource()
def init_chain():
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
    llm = OpenAI(temperature=0.4, openai_api_key=OPENAI_API_KEY, verbose=True)
    chain = VectorDBQA.from_chain_type(llm, chain_type="stuff", vectorstore=vectordb, return_source_documents=True)
    return chain

chain = init_chain()
st.markdown("# Farnam Street QA")
input_text = st.text_area(" ", key="name")
if input_text:
    result = chain(input_text)

    st.write(result["result"])
    st.markdown("---")
    st.markdown("## Sources:")
    for i in result["source_documents"]:
        st.write(i.metadata["source"].split('/')[-1].split('.')[0])
        st.write(filename_to_url(i.metadata["source"]))