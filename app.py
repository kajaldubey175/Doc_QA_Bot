import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
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
        extracted = page.extract_text()
        if extracted:
            text += extracted
        
    # 2. Split Text into Chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    
    # 3. Create Embeddings & Vector Store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    
    # 4. Ask Question
    user_question = st.text_input("Ask a question about your document:")
    
    if user_question:
        docs = vector_store.similarity_search(user_question)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
        response = llm.invoke(f"Context:\n{context}\n\nQuestion: {user_question}\nAnswer:")
        
        st.write("### 🤖 Answer:")
        st.write(response.content)

elif not api_key:
    st.info("Please enter your API key in the sidebar to start asking questions.")
