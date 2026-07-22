# 📚 Document Q&A System

An interactive Document Question-Answering system built using **Streamlit**, **LangChain**, **FAISS**, and **OpenAI**. Upload any PDF document and instantly ask questions to retrieve precise answers based on its content.

---

## ✨ Features
- 📄 **PDF Text Extraction**: Seamlessly reads and processes uploaded PDF documents.
- ✂️ **Smart Text Chunking**: Breaks large text into optimal chunks for accurate vector retrieval.
- ⚡ **Vector Search**: Uses **FAISS** for ultra-fast similarity search across chunks.
- 💬 **Context-Aware Answers**: Leverages Large Language Models (LLMs) to answer user questions purely based on document context.

---

## 🛠️ Tech Stack
- **Frontend UI**: Streamlit
- **LLM Framework**: LangChain
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Embeddings & LLM**: OpenAI API (`gpt-3.5-turbo`)

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.9+** installed and an active **OpenAI API Key**.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/document-qa-system.git
cd document-qa-system
```
### 2. Create a Virtual Environment
````
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
````
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Set Up Environment Variables
OPENAI_API_KEY=your_openai_api_key_here
### 5. Run the Application
streamlit run app.py
### 📸 Demo Workflow
1. Upload Document: Upload your PDF file through the sidebar uploader.
2. Processing: The application extracts text, creates chunks, and generates vector embeddings.
3. Ask Questions: Type any query related to your uploaded document in the input box.
4. Get Answers: Receive instant, accurate responses sourced directly from the document context.
## 🌐 Live Application
You can access and test the live application here:  
👉 **[Click Here to Open App](https://docappbot-vzgh8dzthvuswzkatbuusy.streamlit.app/)**
