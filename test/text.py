from pymin import *

frames = 20
def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    # scale(1,-1)
    background(255)
    no_stroke()
    fill(0)
    # Text("delta",(0,0), size = 230, font = "i")
    Text("delta",(0,0), size = 230, font = "n")




    if frame_count > frames:
        exit()

if __name__ == '__main__':
    run(frame_rate=30)
