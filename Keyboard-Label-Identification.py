import pytesseract
import cv2
from PIL import Image

# Path to tesseract executable (you might need to specify the path if it's not in your PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update path accordingly

# Function to process image and extract key labels row by row
def extract_keyboard_keys(image_path):
    # Step 1: Read the image using OpenCV
    img = cv2.imread(image_path)
    
    # Step 2: Convert the image to grayscale (improves OCR accuracy)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Step 3: Apply thresholding to make the text more distinguishable
    _, thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)
    
    # Step 4: Use pytesseract to do OCR on the processed image
    extracted_text = pytesseract.image_to_string(thresh_img, config='--psm 6')  # psm 6 is for block of text
    
    # Step 5: Post-process the extracted text
    # Split by lines and filter out empty lines
    rows = [line.strip() for line in extracted_text.split("\n") if line.strip()]
    
    # Step 6: Print the results in a format similar to your desired output
    print("Extracted Key Labels:")
    for i, row in enumerate(rows):
        print(f"Row{i+1}: {row}")

# Example usage
image_path = r"C:\Users\ImanOwais\source\repos\PYTHON\PythonAPIAspDotNet\static\KeyboardImages\keyboard black1.PNG"  # Path to your image
extract_keyboard_keys(image_path)