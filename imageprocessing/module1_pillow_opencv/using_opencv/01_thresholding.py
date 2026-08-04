"""Separate foreground from background.
imread() reads the image.
cvtColor() converts BGR to grayscale.
threshold() maps pixels to 0 or 255.
"""
from pathlib import Path
import cv2
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"document.png"))
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,180,255,cv2.THRESH_BINARY)
cv2.imwrite(str(B/"outputs"/"binary_threshold.png"),binary)
print("Saved threshold result")
