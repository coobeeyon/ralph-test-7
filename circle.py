from PIL import Image, ImageDraw

WIDTH = 809
HEIGHT = 500
PERIWINKLE = (204, 204, 255)
WHITE = (255, 255, 255)

img = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

radius = HEIGHT // 4
cx, cy = WIDTH // 2, HEIGHT // 2
draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=PERIWINKLE)

img.save("output.png")
