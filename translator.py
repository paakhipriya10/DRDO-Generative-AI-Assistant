from transformers import MarianMTModel, MarianTokenizer

# Model for English ↔ Hindi
en_to_hi_model_name = "Helsinki-NLP/opus-mt-en-hi"
hi_to_en_model_name = "Helsinki-NLP/opus-mt-hi-en"

# Load models and tokenizers
en_hi_tokenizer = MarianTokenizer.from_pretrained(en_to_hi_model_name)
en_hi_model = MarianMTModel.from_pretrained(en_to_hi_model_name)

hi_en_tokenizer = MarianTokenizer.from_pretrained(hi_to_en_model_name)
hi_en_model = MarianMTModel.from_pretrained(hi_to_en_model_name)


def detect_language(text: str) -> str:
    # Simple heuristic: if Hindi characters exist, assume it's Hindi
    for ch in text:
        if '\u0900' <= ch <= '\u097F':
            return "hi"
    return "en"


def translate_text(text: str) -> str:
    language = detect_language(text)

    if language == "en":
        tokenizer = en_hi_tokenizer
        model = en_hi_model
    else:
        tokenizer = hi_en_tokenizer
        model = hi_en_model

    inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs, max_length=128)
    output = tokenizer.decode(translated[0], skip_special_tokens=True)

    return output
