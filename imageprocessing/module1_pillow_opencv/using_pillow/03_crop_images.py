"""Crop a required region.
crop((left, top, right, bottom)) extracts a rectangle.
"""
from pathlib import Path
from PIL import Image
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png")
crop=im.crop((220,50,440,260))
crop.save(B/"outputs"/"cropped_region.png")
print("Saved crop:",crop.size)
