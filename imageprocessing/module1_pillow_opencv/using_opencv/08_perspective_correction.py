"""Correct document perspective.
getPerspectiveTransform() calculates a matrix from four source and destination points.
warpPerspective() applies the transformation.
"""
from pathlib import Path
import cv2, numpy as np
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"document.png"))
src=np.float32([[40,30],[660,30],[660,470],[40,470]])
dst=np.float32([[0,0],[619,0],[619,449],[0,449]])
matrix=cv2.getPerspectiveTransform(src,dst)
result=cv2.warpPerspective(im,matrix,(620,450))
cv2.imwrite(str(B/"outputs"/"perspective_corrected.png"),result)
print("Saved corrected document")
