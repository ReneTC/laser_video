from pymin import *

frames = 250


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


strope = Strope()
phot1 = Photon(Vector(280,0),Vector(-3,-1),15)
photons = [phot1]
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
    draw_line(vert2,vert3,time)
    draw_line(vert3,vert4,time)
    draw_line(vert4,vert1,time)

    for p in reversed(photons):
        no_stroke()
        p.show()
        if p.pos[0] > 700:
            p.dir[0] = -1*p.dir[0]
        elif p.pos[0] < -700:
            p.dir[0] = -1*p.dir[0]
        elif p.pos[1] > 250-15 or p.pos[1] < - 250+10:
            photons.remove(p)

    with push_style():
        stroke(5)
        scale_in_out(0,999)
        fill('#dadada')
        rect((-720, -250), 20, 500)
        fill('#dadada')
        rect((700, -250), 20, 500)

    if frame_count > frames:
        # to_gif()
        exit()

    saver()

run()
