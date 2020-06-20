from pymin import *

frames = 100

class Atom:
    def __init__(self):
        self.pos = Vector(0,0)
        self.excited = 0

        self.n0 = 400
        self.n1 = 600

    def show(self):
        no_stroke()

        center = Vector(0,0)
        # proton
        with push_style():
            fill('#dadada')
            with push_matrix():
                scale_in(0)
                circle(center,100)
                fill(0)
                Text("N",(0,20),size=30)
        # energy levels
        with push_style():
            stroke_weight(5)
            stroke(0)
            fill(0,0,0,0)
            with push_matrix():
                scale_in(0)
                circle(center,self.n0)
            with push_matrix():
                scale_in(0)
                circle(center,self.n1)

        fill('#dadada')
        with push_matrix():
            if self.excited == 0:
                translate(0,self.n0/2)
            else:
                translate(0,self.n1/2)
            with push_matrix():
                scale_in(0)
                circle((0,0),50)
                fill(0)
                Text("e",(0,20),size=30)




def setup():
    size(width, height)


atom = Atom()

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    scale(1.2)
    flush_scene(80)
    atom.show()
    stroke(100)
    stroke_weight(3)
    time = 20
    vert1 = (-100,150)
    vert2 = (100,150)
    vert3 = (100,350)
    vert4 = (100-200,350)
    draw_line(vert1,vert2,time)
    draw_line(vert2,vert3,time+10)
    draw_line(vert3,vert4,time+20)
    draw_line(vert4,vert1,time+30)

    if frame_count > frames:
        exit()

    # saver()

run()
# to_gif()
