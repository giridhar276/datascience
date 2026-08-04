"""Measure objects in pixels.
findContours() locates objects.
contourArea() calculates area.
arcLength() calculates perimeter.
boundingRect() gives x, y, width and height.
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
    area=cv2.contourArea(c)
    if area<500: continue
    perimeter=cv2.arcLength(c,True)
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(result,(x,y),(x+w,y+h),(0,0,0),2)
    text=f"W:{w} H:{h} A:{int(area)} P:{int(perimeter)}"
    cv2.putText(result,text,(x,max(y-8,15)),cv2.FONT_HERSHEY_SIMPLEX,0.42,(0,0,0),1)
cv2.imwrite(str(B/"outputs"/"object_measurement.png"),result)
print("Saved measurements")
