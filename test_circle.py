import subprocess
import os
from PIL import Image

GOLDEN_RATIO = 1.618

def setup_module():
    """Run circle.py to generate output.png before tests."""
    subprocess.run(["python3", "circle.py"], check=True)

def test_output_exists():
    assert os.path.isfile("output.png")

def test_aspect_ratio():
    img = Image.open("output.png")
    ratio = img.width / img.height
    assert abs(ratio - GOLDEN_RATIO) < 0.01

def test_center_pixel_is_periwinkle():
    img = Image.open("output.png")
    cx, cy = img.width // 2, img.height // 2
    assert img.getpixel((cx, cy)) == (204, 204, 255)

def test_corner_pixel_is_white():
    img = Image.open("output.png")
    assert img.getpixel((0, 0)) == (255, 255, 255)
