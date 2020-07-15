from pymin import *
import sys
word = sys.argv[1]
frames = 60


width = 1200
height = 250
def setup():
    size(width, height)



def draw():
    translate(width/2,height/2)
    translate(0,interpolate(-50,0,-5))
    background(255)
    scale(1,-1)
    fill(interpolate(255,0,-7))
    no_stroke()
    Text(word,(0,30),size=60)
    saver(word)
    if frame_count > frames:
        # to_gif()
        exit()
run()
