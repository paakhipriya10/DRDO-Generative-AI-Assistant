# code_analyzer.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load CodeT5-small model
model_name = "Salesforce/codet5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

explainer = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def explain_code(code: str) -> str:
    """
    Uses CodeT5 to generate explanation for the provided code snippet.
    Args:
        code (str): Input code snippet.
    Returns:
        str: Code explanation.
    """
    try:
        input_text = f"Explain this code: {code}"
        result = explainer(input_text, max_length=128, do_sample=False)
        return result[0]["generated_text"]
    except Exception as e:
        return f"Code analysis error: {e}"
