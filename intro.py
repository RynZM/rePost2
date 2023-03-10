# import cv2 
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# img = cv2.imread('C:\\users\\RyanZ\\OneDrive\\Documents\\Coding\\rePost\\Python\\rePost2\\image.jpg')

# custom_config = r'--oem 3 --psm 6'
# pytesseract.image_to_string(img, config=custom_config)




from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

print(pytesseract.image_to_string(r'C:\\users\\RyanZ\\OneDrive\\Documents\\Coding\\rePost\\Python\\rePost2\\random.png'))




# import pytesseract
# from PIL import Image


# def print_text():
#     print(pytesseract.image_to_string('r:\\users\\RyanZ\\OneDrive\\Documents\\Coding\\rePost\\Python\\rePost2\\random.png'))
