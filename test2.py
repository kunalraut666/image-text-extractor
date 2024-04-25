import pytesseract
from PIL import Image, ImageTk
img = Image.open('refresh.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
result = pytesseract.image_to_string(img)
print(result)