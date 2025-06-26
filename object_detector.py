import torch
from PIL import Image
import numpy as np
import io

# Load YOLOv5s model (CPU-friendly, small variant)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
model.eval()

def detect_objects(uploaded_file):
    # Load image
    image = Image.open(uploaded_file).convert("RGB")

    # Run inference
    results = model(image)

    # Convert results to image with bounding boxes
    results.render()  # updates results.imgs with boxes
    detected_img = Image.fromarray(results.imgs[0])

    return detected_img
