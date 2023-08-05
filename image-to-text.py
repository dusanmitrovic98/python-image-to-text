import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        extracted_text = pytesseract.image_to_string(gray_image)
        return extracted_text.strip()
    except Exception as e:
