#  DRDO Gen-AI Assistant

An intelligent,offline-capable Gen-AI assistant built for DRDO staff and researchers to semantically search, summarize, and interact with DRDO documents and lab data.It also provides functionalities like object(threat) detection,multilingual translation,image similarity search and code analysis.It is going to be built  without any external API calls to ensure safety of confidential DRDO data.

---

##  Problem Statement

Navigating vast volumes of DRDO research data, technical PDFs, lab profiles, and classified reports can be time-consuming and inefficient for researchers, interns, and analysts. Manual information retrieval not only delays decision-making but also increases the chances of overlooking critical insights. Furthermore, due to strict confidentiality protocols, DRDO data cannot be uploaded to external platforms like OpenAI or Gemini, necessitating a fully offline, secure, and locally-deployable AI assistant tailored to DRDO’s internal ecosystem.

---

##  Solution Approach

We are building an offline-capable chatbot-based web application without external API calls for security that:
- Scrapes, processes, and indexes DRDO data offline
- Uses NLP and semantic embeddings to understand and answer queries
- Summarizes long technical documents
- Supports image and code intelligence tasks in later stages
- Provides bilingual translation of techincal documents(Hindi to English and English to Hindi)
- Does Code analysis of scripts
- Supports Image-based searching and object/threat detection in images

The assistant performs all inference locally using CPU-friendly, lightweight models, making it privacy-safe and deployable even in restricted environments.

---

###  Use Cases

#### 1. Chatbot Assistant *(NLP + Retrieval-Augmented Generation)*
- **Function:** Responds to queries related to DRDO labs, technologies, and reports using semantic search and summarization.  
- **Use Case:** Helps new researchers or interns onboard quickly by providing accurate information from internal documents.

#### 2. Object Detection *(Computer Vision)*
- **Function:** Detects and labels objects in images using YOLOv5.  
- **Use Case:** Analyze surveillance footage or drone images in defense operations.

#### 3. Image Similarity Search *(CLIP + FAISS)*
- **Function:** Finds visually similar images from a reference database.  
- **Use Case:** Match captured images to database visuals for threat detection, target identification, or equipment verification.

#### 4. Code Analyzer *(Heuristics and Generative-AI)*
- **Function:** Summarizes Python code into simple language using parsing heuristics and BART.  
- **Use Case:** Assists DRDO developers, interns, or analysts in understanding legacy scripts or debugging quickly.

#### 5. Language Translation *(Helsinki-NLP’s opus-mt)*
- **Function:** Translates between English and Hindi using Helsinki-NLP’s opus-mt model.  
- **Use Case:** Helps in bi-lingual communication across DRDO labs and translating technical material or reports.

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

##  How to Run(Ensure Python is properly installed on your system)

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
   pip install -r requirements.txt #Works on any Python IDE with virtual environment support.
5. Do scraping using scraper.py and dowload PDFs and images for dummy database or directly use dummy database stored in data folder
6. Run setup:
   ```bash
   python setup.py  
7. Launch app:
   ```bash
   streamlit run app.py
8. The app will launch at:
   ```bash
   http://localhost:8501
---

##  Intern Info

> **Intern:** Paakhi Priya  
> **Mentor Lab:** SSPL, DRDO  
> **Project Duration:** 8 weeks  



