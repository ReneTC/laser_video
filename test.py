from p5 import *

def setup():
        size(640, 360)

def draw():
    no_stroke()

    background(0)

    fill(255)
    scale(1,0.1)
    rect((0, 0), 200, 200)


if __name__ == '__main__':
  run()
