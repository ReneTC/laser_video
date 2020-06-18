from pymin import *

frames = 190

def setup():
    size(width, height)


atom = Atom()
strope = Strope()

def draw():
    fps_counter()
    translate(width/2,height/2)

    background(255)
    scale(1,-1)
    stroke(0)
    stroke_weight(4)
    time = 0

    draw_box()

    strope.show()
    Text(str(frame_count), (0,-300),size=50)
    # if frame_count % 30 == 0:
    #     print(frame_count, "flash")
    #     strope.flash()
    if frame_count == 30:
        print(frame_count, "flash")
        strope.flash()

    atom.show()

    if frame_count > frames:
        exit()

run(frame_rate=30)
