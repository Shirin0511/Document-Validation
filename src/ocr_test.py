from PIL import Image
import pytesseract

image_path="data/processed/pan/pan_0.png"

img= Image.open(image_path)
text=pytesseract.image_to_string(img)

print(text)