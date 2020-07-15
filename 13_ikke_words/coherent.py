from pymin import *
import random

frames = 200

class Photon2:
    def __init__(self,pos,direc,energy):
        self.pos = pos
        self.dir = direc.normalize()
        self.energy = energy

        self.created = frame_count

    def show(self):
        velocity = 0
        self.pos = self.pos + self.dir * velocity
        with push_matrix():
            translate(self.pos[0],self.pos[1])
            angle = atan2(self.dir[1], self.dir[0])
            rotate(angle)
            with push_style():
                col = (0,0,0)
                if self.energy == 100:
                    col = (235, 64, 52)
                if self.energy == 300:
                    col = (89,0,152)
                alpha_c = interpolate(0,255,self.created,duration = 20)
                fill(*col,alpha_c)
                stroke(*col,alpha_c)
                stroke_weight(3)
                photon()


def setup():
    size(width, height)


phot1 = Photon2(Vector(-300,0),Vector(1,0),100)
phot2 = Photon2(Vector(-300,100),Vector(1,0),100)
phot3 = Photon2(Vector(500-50,0),Vector(1,0),100)
phot4 = Photon2(Vector(500+50,100),Vector(1,0),100)
photons = [phot2,phot1,phot3,phot4]

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    scale(1.2)

    no_stroke()
    fill(240)
    rect((+1000-width/2, height/2), width/2, -4*height)
    fill(0)
    Text("Coherent",(-400,420),size =45)
    Text("Not Coherent",(420,420),size =45)

    #show atoms
    # show photons
    for p in photons:
        p.show()

#
    saver()
    if frame_count > frames:
        # to_gif()
        exit()


#
run(frame_rate=30)
