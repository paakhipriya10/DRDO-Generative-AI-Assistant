# image_similarity.py

import os
import torch
import faiss
import pickle
import numpy as np
from PIL import Image
from torchvision import transforms
from transformers import CLIPProcessor, CLIPModel

# Directories
IMAGE_DIR = "data/image_gallery"
FAISS_INDEX_FILE = "faiss_store/image_index.faiss"
IMAGE_META_FILE = "faiss_store/image_paths.pkl"

# Load lightweight CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16").to(device)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

def get_image_features(image_path):
    """
    Compute CLIP features for a single image.
    """
    image = Image.open(image_path).convert("RGB")
    inputs = clip_processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        features = clip_model.get_image_features(**inputs)
    return features.cpu().numpy().flatten()

def build_image_index():
    """
    Builds FAISS index from images in IMAGE_DIR.
    """
    os.makedirs("faiss_store", exist_ok=True)
    image_paths = [os.path.join(IMAGE_DIR, fname) for fname in os.listdir(IMAGE_DIR)
                   if fname.lower().endswith((".jpg", ".jpeg", ".png"))]

    features = []
    for path in image_paths:
        vec = get_image_features(path)
        features.append(vec)

    features = np.stack(features)
    index = faiss.IndexFlatL2(features.shape[1])
    index.add(features)

    faiss.write_index(index, FAISS_INDEX_FILE)
    with open(IMAGE_META_FILE, 'wb') as f:
        pickle.dump(image_paths, f)

    print(f"[✔] Built image similarity index with {len(image_paths)} images.")

def search_similar_images(query_image_path, top_k=3):
    """
    Finds top_k visually similar images to the query image.
    """
    if not os.path.exists(FAISS_INDEX_FILE):
        build_image_index()

    query_vec = get_image_features(query_image_path).reshape(1, -1)
    index = faiss.read_index(FAISS_INDEX_FILE)

    with open(IMAGE_META_FILE, 'rb') as f:
        image_paths = pickle.load(f)

    distances, indices = index.search(query_vec, top_k)
    return [image_paths[i] for i in indices[0] if i < len(image_paths)]
