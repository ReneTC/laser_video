from p5 import *

def setup():
        size(640, 360)

def draw():
    no_stroke()

    background(0)

    fill(255)
    offset = 20
    rotate(angle+PI/4)
    triangle((offset*0.5, offset),(-offset/2, offset),(0.5,-offset/2))


if __name__ == '__main__':
  run()
