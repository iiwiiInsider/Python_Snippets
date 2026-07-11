# dot_circle.py
# Requires: colorgram.py (pip install colorgram.py)
# Place your image in the same folder and name it "image.jpg" (or change the filename below).

import turtle
import colorgram
import random
import math

# ---------- Configuration ----------
IMAGE_FILE = 'image.jpg'      # change if your image has a different name
NUM_COLORS = 30               # how many colors to extract from the image
DOT_SIZE = 20                 # diameter of each dot in pixels
SPACING = 40                  # grid spacing between dot centers
RADIUS = 300                  # radius of the circular area to fill with dots
SCREEN_SIZE = 800             # turtle screen size (square)
BACKGROUND_COLOR = 'white'
# -----------------------------------

def extract_palette(image_file, n_colors):
    """Extract RGB palette from an image using colorgram."""
    colors = colorgram.extract(image_file, n_colors)
    palette = []
    for c in colors:
        r, g, b = c.rgb.r, c.rgb.g, c.rgb.b
        palette.append((r, g, b))
    # Remove near-white colors to keep dots colorful
    palette = [col for col in palette if not (col[0] > 240 and col[1] > 240 and col[2] > 240)]
    if not palette:
        # fallback palette
        palette = [(230, 57, 70), (29, 53, 87), (69, 123, 157), (168, 218, 220), (241, 250, 238)]
    return palette

def draw_dot_circle(palette):
    """Draw a circular grid of dots using turtle, using colors from palette."""
    screen = turtle.Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Dot Circle")
    screen.colormode(255)

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed('fastest')

    # Use tracer to speed up drawing
    screen.tracer(0, 0)

    # center at (0,0). We'll iterate a grid and only draw dots inside the circle radius.
    start = -RADIUS
    end = RADIUS
    y = start
    while y <= end:
        x = start
        while x <= end:
            # check if the point is inside the circle
            if math.hypot(x, y) <= RADIUS:
                t.goto(x, y)
                color = random.choice(palette)
                t.dot(DOT_SIZE, color)
            x += SPACING
        y += SPACING

    screen.update()
    # keep window open until closed by user
    turtle.done()

if __name__ == '__main__':
    palette = extract_palette(IMAGE_FILE, NUM_COLORS)
    draw_dot_circle(palette)
