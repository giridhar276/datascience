"""Rotate and flip images.
rotate() changes orientation.
expand=True prevents clipping.
transpose(FLIP_LEFT_RIGHT) mirrors horizontally.
"""
from pathlib import Path
from PIL import Image
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png")
im.rotate(30,expand=True,fillcolor="white").save(B/"outputs"/"rotated.png")
im.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save(B/"outputs"/"flipped.png")
print("Saved rotated and flipped images")
