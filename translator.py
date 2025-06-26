# translator.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load IndicTrans2 model
model_name = "ai4bharat/indictrans2-en-translite"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

translator = pipeline("translation", model=model, tokenizer=tokenizer)

def translate_text(text: str) -> str:
    """
    Translates Indian language text to English using IndicTrans2.
    Args:
        text (str): Input text in Indian language.
    Returns:
        str: Translated English text.
    """
    try:
        result = translator(text, max_length=512)
        return result[0]["translation_text"]
    except Exception as e:
        return f"Translation error: {e}"
