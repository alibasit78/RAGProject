import re

text_pattern = re.compile(r"[^\w\s\.,!?]", re.IGNORECASE)
multi_space_pattern = re.compile(r"\s+", re.IGNORECASE)

def clean_text(text):
    text = text_pattern.sub(" ", text)
    text = multi_space_pattern.sub(" ", text)
    return text.strip()