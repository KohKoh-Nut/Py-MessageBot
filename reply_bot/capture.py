import cv2
import numpy as np
import pytesseract
import pyautogui

class ScreenCapture:
    def __init__(self, region=None):
        self.region = region

    def set_region(self, region):
        """Set the region to capture."""
        self.region = region

    def capture_text_from_region(self):
        """Capture text from the selected screen region."""
        if not self.region:
            return ""

        x, y, w, h = self.region
        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        image = np.array(screenshot)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        extracted_text = pytesseract.image_to_string(thresh, lang="eng")
        return extracted_text.strip()
