"""Classify basic shapes.
arcLength() calculates perimeter.
approxPolyDP() reduces contour points.
The number of vertices identifies triangle, rectangle or circle-like shapes.
"""
from pathlib import Path
import cv2
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"shapes.png"))
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)
contours,_=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
result=im.copy()
for c in contours:
    if cv2.contourArea(c)<500: continue
    p=cv2.arcLength(c,True)
    a=cv2.approxPolyDP(c,0.03*p,True)
    n=len(a)
    name="Triangle" if n==3 else "Rectangle" if n==4 else "Circle/Other"
    x,y,w,h=cv2.boundingRect(a)
    cv2.putText(result,name,(x,max(y-8,15)),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2)
cv2.imwrite(str(B/"outputs"/"shape_detection.png"),result)
print("Saved shape detection")
