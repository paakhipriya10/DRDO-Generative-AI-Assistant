from PIL import Image
import os
import torch
import numpy as np
from transformers import CLIPProcessor, CLIPModel
import faiss

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Preload image index and paths (assume they're stored in 'indexed_images')
image_dir = "data/image_gallery"
image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith((".jpg", ".png"))]

# Generate embeddings for database
def get_image_embedding(image):
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        embeddings = model.get_image_features(**inputs)
    return embeddings[0].cpu().numpy()

# Build FAISS index (assumes run once)
def build_index():
    vectors = []
    for path in image_paths:
        img = Image.open(path).convert("RGB")
        emb = get_image_embedding(img)
        vectors.append(emb)
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(np.array(vectors))
    return index, vectors

index, _ = build_index()

def search_similar_images(query_img):
    image = Image.open(query_img).convert("RGB")
    query_vector = get_image_embedding(image).reshape(1, -1)
    _, indices = index.search(query_vector, k=1)
    top_img_path = image_paths[indices[0][0]]
    top_img_name = os.path.splitext(os.path.basename(top_img_path))[0]
    return top_img_path, top_img_name
