"""Remove noise.
medianBlur() replaces each pixel with the median of neighbouring pixels.
It is effective for salt-and-pepper noise.
"""
from pathlib import Path
import cv2
B=Path(__file__).parent
im=cv2.imread(str(B/"images"/"noisy_image.png"))
clean=cv2.medianBlur(im,5)
cv2.imwrite(str(B/"outputs"/"noise_removed.png"),clean)
print("Saved cleaned image")
