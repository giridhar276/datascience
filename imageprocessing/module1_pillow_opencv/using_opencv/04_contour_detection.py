"""Detect and draw object outlines.
threshold() creates a binary mask.
findContours() extracts boundaries.
drawContours() draws them.
"""
from pathlib import Path
import cv2
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"shapes.png"))
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)
contours,_=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
result=im.copy()
cv2.drawContours(result,contours,-1,(0,255,255),3)
cv2.imwrite(str(B/"outputs"/"contours.png"),result)
print("Contours:",len(contours))
