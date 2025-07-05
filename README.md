#  DRDO Gen-AI Assistant

An intelligent,offline-capable Gen-AI assistant built for DRDO staff and researchers to semantically search, summarize, and interact with DRDO documents and lab data.It also provides functionalities like object(threat) detection,multilingual translation,image similarity search and code analysis.It is going to be built  without any external API calls to ensure safety of confidential DRDO data.

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
- Provides bilingual translation of techincal documents
- Does Code analysis of scripts
- Supports Image-based searching and object/threat detection in images

The assistant performs all inference locally using CPU-friendly, lightweight models, making it privacy-safe and deployable even in restricted environments.

---

## Tech Stack

- **Frontend:** Streamlit (custom-styled UI with tabbed navigation)
- **Dummy Database**: curated through offline web scraping using the BeautifulSoup Python library
- **ML Framework**: PyTorch
- **Backend Models:**
  - *Q/A:* DistilBERT (SQuAD fine-tuned)
  - *Summarization:* DistilBART (CNN/DailyMail)
  - *Embeddings:* SentenceTransformers (MiniLM)
- **Data Indexing:** FAISS (for semantic search)
- **Scraping:** Offline web scraping using BeautifulSoup
- **Image & Code Models:** 
  - YOLOv5s (Object Detection)
  - CLIP + FAISS (Image Similarity)
  - Helsinki-NLP’s opus-mt model (Indian Language Translation)(IndicTrans2 model unavailable)
  - Python-based rules/parsing heuristics along with BART(a powerful AI model) as a backup. (Code Analysis)(switched from CodeT5 model)

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
- Helsinki-NLP’s opus-mt model multilingual translation (due to unavaibility of IndicTrans2 model)
- Code analysis using python-based rules/parsing heuristics(switched from CodeT5 model)

---

##  Progress Timeline

- **Week 1-2:** Set up data pipeline and semantic search
- **Week 3-4:** Integrated summarization, Q/A, PDF support
- **Week 5-6:** UI polish + testing existing features
- **Week 7-8:** Add vision and code-based features + polish

---

##  How to Run

1. Clone the project folder using Git or download it manually:
   ```bash
   git clone https://github.com/paakhipriya10/DRDO-Generative-AI-Assistant.git
   ```
   ```bash
   cd DRDO-Generative-AI-Assistant
   ```
2. Create a virtual python environment and activate it:
   ```bash
   python -m venv venv #to create a virtual environment
   ```
   ```bash
   venv\Scripts\activate #to activate the environment on Windows
   ```
   ```bash
   source venv/bin/activate #to activate on macOS/Linux
   ```
4. Install all required libraries using:
   ```bash
   pip install -r requirements.txt
5. Do scraping using scraper.py and dowload PDFs or directly use dummy database stored in data folder
6. Run setup:
   ```bash
   python setup.py  
7. Launch app:
   ```bash
   streamlit run app.py
   

---

##  Intern Info

> **Intern:** Paakhi Priya  
> **Mentor Lab:** SSPL, DRDO  
> **Project Duration:** 8 weeks  



