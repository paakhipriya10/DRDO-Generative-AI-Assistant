#  DRDO Gen-AI Assistant

An intelligent Gen-AI assistant built for DRDO staff and researchers to semantically search, summarize, and interact with DRDO documents and lab data.It also provides functionalities like object(threat) detection,multilingual translation,image similarity search and code analysis.It is going to be built right from scratch without any external API calls to ensure safety of confidential DRDO data.

---

##  Problem Statement

Navigating through large volumes of DRDO research data, PDFs, lab descriptions, and reports manually is time-consuming and inefficient. There is a need for an intelligent assistant that can help researchers quickly retrieve relevant insights.Moreover,its not possible to upload confidential DRDO data on OpenAI or Gemini due to security concerns.

---

##  Solution Approach

We are building an offline-capable chatbot-based web application without external API calls for security that:
- Scrapes, processes, and indexes DRDO data offline
- Uses NLP and semantic embeddings to understand and answer queries
- Summarizes long technical documents
- Supports image and code intelligence tasks in later stages

The assistant performs all inference locally using CPU-friendly, lightweight models, making it privacy-safe and deployable even in restricted environments.

---

## Tech Stack

- **Frontend:** Streamlit (custom-styled UI with tabbed navigation)
- **Backend Models:**
  - *Q/A:* DistilBERT (SQuAD fine-tuned)
  - *Summarization:* DistilBART (CNN/DailyMail)
  - *Embeddings:* SentenceTransformers (MiniLM)
- **Data Indexing:** FAISS (for semantic search)
- **Scraping:** Offline web scraping using BeautifulSoup
- **Image & Code Models:** (Upcoming)
  - YOLOv5s (Object Detection)
  - CLIP + FAISS (Image Similarity)
  - IndicTrans2 (Indian Language Translation)
  - CodeT5-small (Code Explanation)

---

##  Features

###  Implemented & Under Testing (As of June-End)
- Chatbot UI with chat history
- Offline web scraping for DRDO + Wikipedia content
- PDF parsing and summarization
- Semantic Search using FAISS
- Q/A system using local DistilBERT
- Summarization of long answers (DistilBART)
- Dynamic multi-tabbed Streamlit interface

###  Under Integration (To be completed by July-End)
- Object detection from uploaded images (YOLOv5s)
- CLIP-based image similarity search
- IndicTrans2-based multilingual translation
- Code analysis using CodeT5-small

---

##  Progress Timeline

- **Week 1-2:** Set up data pipeline and semantic search
- **Week 3-4:** Integrated summarization, Q/A, PDF support
- **Week 5-6 (Now):** UI polish + testing existing features
- **Week 7-8 (Planned):** Add vision and code-based features + polish

---

##  How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Run setup: `python setup.py` (scrapes + builds FAISS index)
3. Launch app: `streamlit run app.py`

---

##  Intern Info

> **Intern:** Paakhi Priya  
> **Mentor Lab:** SSPL, DRDO  
> **Project Duration:** 8 weeks  
> **Title:** *Building a Gen-AI Assistant for DRDO Research Support*


