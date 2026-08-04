"""Add image borders.
ImageOps.expand() adds padding of a selected width and colour.
"""
from pathlib import Path
from PIL import Image,ImageOps
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png")
ImageOps.expand(im,border=25,fill="black").save(B/"outputs"/"bordered.png")
print("Saved bordered image")
