from typing import List
from pathlib import Path
from pil_utils import BuildImage
from PIL.Image import Image as IMG

from meme_generator import add_meme
from meme_generator.utils import save_gif


img_dir = Path(__file__).parent / "images"


def wallpaper(images: List[BuildImage], texts, args):
    img = images[0].convert("RGBA").resize((515, 383), keep_ratio=True)
    frames: List[IMG] = []
    for i in range(8):
        frames.append(BuildImage.open(img_dir / f"{i}.png").image)
    for i in range(8, 20):
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(img, (176, -9), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.07)


add_meme("wallpaper", ["墙纸"], wallpaper, min_images=1, max_images=1)
