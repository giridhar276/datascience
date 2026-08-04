"""Add text and logo watermarks.
convert("RGBA") enables transparency.
Image.new("RGBA") creates a transparent overlay.
ImageDraw.Draw().text() adds text.
alpha_composite() merges transparent layers.
paste(..., mask=logo) preserves logo transparency.
"""
from pathlib import Path
from PIL import Image,ImageDraw
B=Path(__file__).parent
im=Image.open(B/"images"/"sample_color.png").convert("RGBA")
logo=Image.open(B/"images"/"logo.png").convert("RGBA")
overlay=Image.new("RGBA",im.size,(255,255,255,0))
ImageDraw.Draw(overlay).text((390,380),"CONFIDENTIAL",fill=(255,0,0,150))
result=Image.alpha_composite(im,overlay)
result.paste(logo,(20,20),logo)
result.save(B/"outputs"/"watermarked.png")
print("Saved watermark")
