import streamlit as st
from agent_core import process_query
from object_detector import detect_objects
from image_similarity import find_similar_images
from code_analyzer import explain_code
from translator import translate_text

# Page config
st.set_page_config(page_title="DRDO Gen-AI Agent", layout="wide")

# Custom styles
st.markdown("""
    <style>
        body { background-color: #f0f4fa; }
        .title {
            text-align: center;
            color: #1e3c72;
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #1e3c72;
        }
        .stTextArea textarea {
            border: 2px solid #1e3c72;
        }
        .stFileUploader label {
            color: #1e3c72;
            font-weight: bold;
        }
        .css-1aumxhk {
            background-color: #dff0d8 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 DRDO Gen-AI Assistant</div>', unsafe_allow_html=True)

# Tabs for features
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧠 Chatbot",
    "📸 Object Detection",
    "🖼️ Image Similarity",
    "💻 Code Analyzer",
    "🌐 Translator"
])

# === Tab 1: Chatbot ===
with tab1:
    st.subheader("Ask about DRDO research, labs, documents, and more")

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Ask your question:")

    if user_input:
        st.session_state.history.append(("user", user_input))
        with st.spinner("Thinking..."):
            response = process_query(user_input)
        st.session_state.history.append(("bot", response))

    for sender, msg in st.session_state.history:
        color = "#cce5ff" if sender == "user" else "#d4edda"
        st.markdown(f"<div style='background-color: {color}; padding:10px; border-radius:10px; margin:5px 0;'>{msg}</div>", unsafe_allow_html=True)

# === Tab 2: Object Detection ===
with tab2:
    st.subheader("Detect objects in images (YOLOv5s)")
    image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="obj-detect")
    if image_file:
        with st.spinner("Detecting..."):
            output_img = detect_objects(image_file)
            st.image(output_img, caption="Detected Objects", use_column_width=True)

# === Tab 3: Image Similarity ===
with tab3:
    st.subheader("Find similar images using CLIP + FAISS")
    query_img = st.file_uploader("Upload query image", type=["jpg", "png"], key="clip-sim")
    if query_img:
        with st.spinner("Finding similar images..."):
            results = find_similar_images(query_img)
            for img_path in results:
                st.image(img_path, caption="Similar Image", use_column_width=True)

# === Tab 4: Code Analyzer ===
with tab4:
    st.subheader("Explain code snippets (CodeT5-small)")
    code_input = st.text_area("Paste your code here:", height=200)
    if code_input:
        with st.spinner("Analyzing code..."):
            explanation = explain_code(code_input)
        st.success(explanation)

# === Tab 5: Translator ===
with tab5:
    st.subheader("Translate Indian language text (IndicTrans2)")
    src_text = st.text_area("Enter text in Hindi, Tamil, etc.:", height=150)
    if src_text:
        with st.spinner("Translating..."):
            translated = translate_text(src_text)
        st.success(f"Translation: {translated}")
