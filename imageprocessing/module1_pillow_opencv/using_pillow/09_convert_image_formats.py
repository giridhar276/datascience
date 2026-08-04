"""Convert image formats.
convert("RGB") ensures JPEG compatibility.
save() infers output type from the extension.
"""
from pathlib import Path
from PIL import Image
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png").convert("RGB")
im.save(B/"outputs"/"converted.jpg",quality=95)
im.save(B/"outputs"/"converted.bmp")
im.save(B/"outputs"/"converted.webp")
print("Saved JPEG, BMP and WEBP")
