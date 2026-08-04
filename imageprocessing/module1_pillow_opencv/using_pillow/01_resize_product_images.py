"""Resize product images.
Image.open() opens a file.
resize() changes dimensions.
LANCZOS gives high-quality downsampling.
save() writes the result.
"""
from pathlib import Path
from PIL import Image
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png")
out=im.resize((320,210),Image.Resampling.LANCZOS)
out.save(B/"outputs"/"resized_product.png")
print(im.size, "->", out.size)
