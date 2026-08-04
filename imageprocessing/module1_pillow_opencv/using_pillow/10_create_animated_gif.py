"""Create an animated GIF.
rotate() creates frames.
save_all=True stores multiple frames.
append_images adds remaining frames.
duration controls speed and loop=0 repeats forever.
"""
from pathlib import Path
from PIL import Image
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png")
frames=[im.rotate(a,fillcolor="white") for a in range(0,360,30)]
frames[0].save(B/"outputs"/"rotation_animation.gif",save_all=True,
               append_images=frames[1:],duration=120,loop=0)
print("Saved animated GIF")
