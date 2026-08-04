"""Create thumbnails.
copy() protects the original.
thumbnail() preserves aspect ratio and fits within a maximum box.
"""
from pathlib import Path
from PIL import Image
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png")
thumb=im.copy()
thumb.thumbnail((180,180))
thumb.save(B/"outputs"/"thumbnail.png")
print("Saved thumbnail:",thumb.size)
