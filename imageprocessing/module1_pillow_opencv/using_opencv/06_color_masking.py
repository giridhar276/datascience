"""Detect red objects using HSV.
cvtColor(...HSV) separates colour from brightness.
inRange() creates masks for selected colour ranges.
bitwise_or() combines red ranges.
bitwise_and() applies the mask.
"""
from pathlib import Path
import cv2, numpy as np
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"shapes.png"))
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
m1=cv2.inRange(hsv,np.array([0,100,100]),np.array([10,255,255]))
m2=cv2.inRange(hsv,np.array([170,100,100]),np.array([180,255,255]))
mask=cv2.bitwise_or(m1,m2)
result=cv2.bitwise_and(im,im,mask=mask)
cv2.imwrite(str(B/"outputs"/"red_object_mask.png"),result)
print("Saved colour mask")
