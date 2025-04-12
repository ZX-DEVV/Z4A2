import pyautogui
import pytesseract
from PIL import Image
import keyboard
import time

# Set up pytesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_chat_text(region=None):
    screenshot = pyautogui.screenshot(region=region)  # region=(x, y, width, height)
    text = pytesseract.image_to_string(screenshot)
    return text.lower()

def send_present():
    keyboard.write("present")
    keyboard.press_and_release("enter")

def monitor_chat():
    print("Monitoring chat... Press Ctrl+C to stop.")
    while True:
        text = get_chat_text(region=(100, 300, 800, 500))  # Adjust based on where your Teams chat appears
        if text.count("present") >= 3:
            print("Detected 'present' 3+ times. Sending response...")
            send_present()
            time.sleep(5)  # wait to avoid spam
        time.sleep(2)  # check every 2 seconds

if __name__ == "__main__":
    monitor_chat()



#pip install pyautogui pytesseract pillow keyboard
