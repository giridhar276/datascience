"""Improve dark images.
ImageEnhance.Brightness changes overall lightness.
ImageEnhance.Contrast changes the difference between light and dark areas.
enhance(factor) uses 1.0 as the original.
"""
from pathlib import Path
from PIL import Image,ImageEnhance
B=Path(__file__).parent
im=Image.open(B/"images"/"dark_image.png")
bright=ImageEnhance.Brightness(im).enhance(1.8)
result=ImageEnhance.Contrast(bright).enhance(1.4)
result.save(B/"outputs"/"brightness_contrast_enhanced.png")
print("Saved enhanced image")
