from pymin import *

class child_circle(PShape):
    def __init__(self):
        super().__init__()


def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    background(255)



    if frame_count > frames:
        exit()

if __name__ == '__main__':
    run(frame_rate=30)
