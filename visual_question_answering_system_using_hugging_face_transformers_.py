# -*- coding: utf-8 -*-
"""Visual Question Answering System Using Hugging Face Transformers .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gW_VVdGUfMomJHVo3SlPGPWvxoiW1kpe
"""

# Install required libraries
!pip install transformers datasets torch torchvision pillow

# Import libraries
import torch
from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import requests
from io import BytesIO
from google.colab import files

# Load pre-trained VQA model and processor
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# Function to perform VQA
def answer_question(image, question):
    # Prepare inputs
    encoding = processor(image, question, return_tensors="pt")

    # Forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    # Get answer
    answer = model.config.id2label[idx]
    return answer

# Upload an image file
uploaded = files.upload()

# Load the uploaded image
image_path = list(uploaded.keys())[0]
image = Image.open(image_path)

# Ask a question
question = input("Please enter your question: ")

# Get the answer
answer = answer_question(image, question)
print(f"Question: {question}\nAnswer: {answer}")