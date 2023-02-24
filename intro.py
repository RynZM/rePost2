from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'




print(pytesseract.image_to_string(Image.open('C:\\Users\\RyanZ\\OneDrive\\Documents\\Coding\\rePost\\Python\\rePost2\\image.jpg')))