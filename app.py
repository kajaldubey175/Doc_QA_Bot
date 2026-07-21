import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
import os

st.set_page_config(page_title="Document Q&A System", page_icon="📚")
st.header("📄 AI Document Q&A System")

api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file and api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    
    # 1. Read PDF
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        
    # 2. Split Text into Chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    
    # 3. Create Embeddings & Vector Store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    
    # 4. Ask Question
    user_question = st.text_input("Ask a question about your document:")
    
    if user_question:
        docs = vector_store.similarity_search(user_question)
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
        chain = load_qa_chain(llm, chain_type="stuff")
        
        response = chain.run(input_documents=docs, question=user_question)
        st.write("### 🤖 Answer:")
        st.write(response)
elif not api_key:
    st.info("Please enter your Gemini API key in the sidebar to proceed.")