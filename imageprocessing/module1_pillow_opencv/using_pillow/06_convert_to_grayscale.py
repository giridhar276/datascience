"""Convert RGB to grayscale.
convert("L") creates an 8-bit single-channel image.
"""
from pathlib import Path
from PIL import Image
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png")
gray=im.convert("L")
gray.save(B/"outputs"/"grayscale.png")
print(im.mode,"->",gray.mode)
