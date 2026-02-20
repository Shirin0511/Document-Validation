import pytesseract
from PIL import Image

def extract_text_from_img(img_path : str):

    try:

        image = Image.open(img_path)
        text = pytesseract.image_to_string(image)
        return text
    
    except Exception as e:
        print("OCR Error:", e)
        return ""
