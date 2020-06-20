from pymin import *

frames = 190


class Strope:
    def __init__(self):
        self.flash = 0
        self.strope_frame = -20

    def show(self):
        with push_matrix():
            translate(700-50,350)
            bredde = 50
            hojde = 50
            vert1 = (-bredde,-hojde)
            vert2 = (bredde,-hojde)
            vert3 = (bredde,hojde)
            vert4 = (-bredde,hojde)
            line(vert1,vert2)
            line(vert2,vert3)
            line(vert3,vert4)
            line(vert4,vert1)
        with push_matrix():
            translate(-700+50,350)
            line(vert1,vert2)
            line(vert2,vert3)
            line(vert3,vert4)
            line(vert4,vert1)

            line((50,30),(1250,30))
            line((50,-30),(1250,-30))

        with push_matrix():
            no_stroke()
            # fill("#fce300")
            translate(0,350)
            # scale(1,0.3)
            rect((0, 0), 1200-4, 60-4, mode="CENTER")


def setup():
    size(width, height)


# atom = Atom((0,0))
strope = Strope()
def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)

    stroke(0)
    stroke_weight(4)
    time = 0

    bredde = 700
    hojde = 250
    vert1 = (-bredde,-hojde)
    vert2 = (bredde,-hojde)
    vert3 = (bredde,hojde)
    vert4 = (-bredde,hojde)
    draw_line(vert1,vert2,time)
    draw_line(vert2,vert3,time+10)
    draw_line(vert3,vert4,time+20)
    draw_line(vert4,vert1,time+30)

    with push_matrix():
        translate(interpolate(-1700,0,130,duration=40),0)
        strope.show()


    # with push_style():
    #     scale_in_out(60,999)
    #     atom.show()
    if frame_count > frames:
        exit()

    # saver()

run()
# to_gif()
