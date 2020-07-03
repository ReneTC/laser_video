from pymin import *

frames = 140

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
                scale_in(30)
                circle(center,self.n0)
            with push_matrix():
                scale_in(50)
                circle(center,self.n1)

        fill('#dadada')
        push_matrix()
        if self.excited == 0:
            translate(0,self.n0/2)
        else:
            translate(0,self.n1/2)
        with push_matrix():
            scale_in(65)
            circle((0,0),50)
            fill(0)
            Text("e",(0,20),size=30)
        reset_matrix()



def setup():
    size(width, height)


atom = Atom()

def draw():
    translate(width/2,height/2)
    translate(interpolate(0,width,120),0)
    background(255)
    scale(1,-1)
    scale(1.2)
    atom.show()
    saver()
    if frame_count > frames:
        to_gif()
        exit()

run()
