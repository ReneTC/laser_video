from pymin import *

frames = 40

def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    background(255)
    stroke_weight(5)


    if frame_count > frames:
        exit()

if __name__ == '__main__':
    run(frame_rate=30)
