"""Create a scanner-like document.
cvtColor() converts to grayscale.
GaussianBlur() reduces noise.
adaptiveThreshold() handles uneven lighting.
"""
from pathlib import Path
import cv2
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"document.png"))
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
scan=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv2.THRESH_BINARY,21,10)
cv2.imwrite(str(B/"outputs"/"scanned_document.png"),scan)
print("Saved scanned document")
