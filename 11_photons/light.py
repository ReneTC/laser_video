from pymin import *
import random

frames = 400


class Photon1:
    def __init__(self,pos,direc,energy):
        self.pos = pos
        self.dir = direc.normalize()
        self.energy = energy

        self.created = frame_count

    def show(self):
        velocity = 6
        self.pos = self.pos + self.dir * velocity
        with push_matrix():
            translate(self.pos[0],self.pos[1])
            angle = atan2(self.dir[1], self.dir[0])
            rotate(angle)
            with push_style():
                col = (0,0,0)
                if self.energy == 100:
                    col = (235, 64, 52,)
                if self.energy == 300:
                    col = (89,0,152)
                # alpha_c = interpolate(0,255,self.created,duration = 20)
                alpha_c = 255
                fill(*col,alpha_c)
                stroke(*col,alpha_c)
                stroke_weight(3)
                photon()


def setup():
    size(width, height)

photons = []
for i in range(0,20):
    photons.append(Photon1(Vector(-1200,+15*i),Vector(1,0),100))
photons2 = []
for i in range(0,20):
    photons2.append(Photon(Vector(-900,15*i),Vector(1,0),15))


def draw():
    translate(width/2,height/2)
    background(255)130
    scale(1,-1)
    scale(1.2)


    # show photons
    for p in photons:
        p.show()
    for p in photons2:
        no_stroke()
        p.show()


    # saver()
    if frame_count > frames:
        exit()


to_gif()
# run(frame_rate=30)
