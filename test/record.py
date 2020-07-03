# from p5 import *
from pymin import *

def setup():
    size(750, 450)
    no_stroke()
    background(204)

def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 50)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(204)

# run()
to_gif()
