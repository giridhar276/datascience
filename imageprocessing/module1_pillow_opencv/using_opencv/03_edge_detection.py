"""Detect object boundaries.
cvtColor() converts to grayscale.
GaussianBlur() reduces noise.
Canny() detects edges using lower and upper thresholds.
"""
from pathlib import Path
import cv2
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"shapes.png"))
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
edges=cv2.Canny(blur,80,180)
cv2.imwrite(str(B/"outputs"/"canny_edges.png"),edges)
print("Saved edges")
