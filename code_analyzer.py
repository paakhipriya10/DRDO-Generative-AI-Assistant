from transformers import BartTokenizer, BartForConditionalGeneration
import torch
import ast

# Load DistilBART model
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def explain_code_heuristically(code_snippet):
    explanation = []

    if "[::-1]" in code_snippet:
        explanation.append("This code reverses a string or list using slicing.")
    if ".append(" in code_snippet:
        explanation.append("This code adds elements to a list using the append method.")
    if "def " in code_snippet:
        explanation.append("This code defines a Python function.")
    if "if " in code_snippet:
        explanation.append("This code uses a conditional statement to check a condition.")
    if "for " in code_snippet:
        explanation.append("This code uses a loop to iterate over a sequence.")
    if "import " in code_snippet:
        explanation.append("This code imports external libraries or modules.")

    return " ".join(explanation) if explanation else None

def explain_code(code_snippet):
    heuristic = explain_code_heuristically(code_snippet)
    if heuristic:
        return heuristic

    # Fallback: use summarization model
    prompt = f"{code_snippet}"
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=150,
        min_length=40,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
