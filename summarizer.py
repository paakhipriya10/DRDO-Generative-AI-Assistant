# summarizer.py

from transformers import pipeline
import logging

# Load the summarization pipeline only once
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    logging.error(f"Failed to load summarization model: {e}")
    summarizer = None

def summarize_text(text, max_summary_length=130):
    """
    Summarizes the given text using HuggingFace's summarization pipeline.

    Parameters:
        text (str): The input text to summarize.
        max_summary_length (int): Max length of the summary output.

    Returns:
        str: Summarized text.
    """
    if summarizer is None or not text.strip():
        return text  # Fallback to original if model failed or input is empty

    try:
        # Truncate input if it exceeds model input size
        trimmed_text = text[:1024]
        summary = summarizer(trimmed_text, max_length=max_summary_length, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        logging.warning(f"Summarization failed: {e}")
        return text
