from pymin import *
width = 600
height = width
frames = 450
def setup():
    size(width, height)


def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)

    stroke(0)
    stroke_weight(4)
    time = 0

    bredde = 200
    hojde = 200
    vert1 = (-bredde,-hojde)
    vert2 = (bredde,-hojde)
    vert3 = (bredde,hojde)
    vert4 = (-bredde,hojde)
    draw_line(vert1,vert2,time)
    draw_line(vert2,vert3,time+10)
    draw_line(vert3,vert4,time+20)
    draw_line(vert4,vert1,time+30)



    if frame_count > frames:
        # to_gif()
        exit()

    saver()

run()
