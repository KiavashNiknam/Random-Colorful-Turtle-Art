# Kiavash Niknam
import turtle as t
from random import random

# Color palette
colors = [
    "red", "blue", "green", "yellow",
    "purple", "orange", "pink", "cyan",
    "white", "magenta"
]

# Generate random turtle art
for i in range(100):

    steps = int(random() * 100)
    angle = int(random() * 360)

    # Choose drawing color
    t.pencolor(colors[i % len(colors)])

    # Move and turn randomly
    t.right(angle)
    t.forward(steps)

# Finish drawing
t.done()
