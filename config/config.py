import os

class Config:
    MODEL_NAME = "facebook/opt-350m"
    OCR_LANG = "eng"

# Ensure Tesseract is set up correctly
if os.name == "nt":
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
