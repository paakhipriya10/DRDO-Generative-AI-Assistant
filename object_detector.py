# object_detector.py

import torch
from PIL import Image
import numpy as np
import io

# Load YOLOv5s model 
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
model.eval()

def detect_objects(uploaded_file):
    # Load image
    image = Image.open(uploaded_file).convert("RGB")

    # Run inference
    results = model(image)

    # Render results to add bounding boxes
    results.render()

    # Convert NumPy array to PIL Image
    detected_img = Image.fromarray(results.ims[0])

    return detected_img
