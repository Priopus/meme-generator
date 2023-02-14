from typing import List
from pathlib import Path
from pil_utils import BuildImage

from meme_generator import add_meme


img_dir = Path(__file__).parent / "images"


def paint(images: List[BuildImage], texts, args):
    img = images[0].convert("RGBA").resize((117, 135), keep_ratio=True)
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(img.rotate(4, expand=True), (95, 107), below=True)
    return frame.save_jpg()


add_meme("paint", ["这像画吗"], paint, min_images=1, max_images=1)
