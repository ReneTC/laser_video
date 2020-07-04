from pymin import *
import random

frames = 160
class Atom:
    def __init__(self):
        self.pos = Vector(0,0)

        self.n0 = 200
        self.n1 = 300

        self.n1_ht = 15

        self.n0_pos = Vector(0,self.n0)
        self.n1_pos = Vector(0,self.n1)

        self.inteaction_frame = -20

        self.n0_occ = 0
        self.n1_occ = 1


    def show(self):
        no_stroke()

        center = Vector(0,0)
        # proton
        with push_style():
            fill('#dadada')
            with push_matrix():
                circle(center,100)
                fill(0)
                Text("N",(0,20),size=30)
        # energy levels circles
        with push_style():
            stroke_weight(5)
            stroke(0)
            fill(0,0,0,0)
            with push_matrix():
                circle(center,self.n0*2)
            with push_matrix():
                circle(center,self.n1*2)

        with push_matrix():
            fill('#dadada')
            translate(0,self.n0)
            scale(interpolate(self.n1_occ,self.n0_occ,self.inteaction_frame,duration = 10))
            circle((0,0),50)
            fill(0)
            Text("e",(0,22,),size=30)

        with push_matrix():
            translate(0,self.n1)
            scale(interpolate(self.n0_occ,self.n1_occ,self.inteaction_frame,duration = 10))
            fill('#dadada')
            circle((0,0),50)
            fill(0)
            Text("e",(0,22,),size=30)



    def interaction(self, photon):
        # get electron pos
        if self.n1 - self.n0 != photon.energy:
            return

        electron_pos = 0
        if self.n1_occ == 0:
            electron_pos = self.n0_pos + self.pos
        if self.n1_occ == 1:
            electron_pos = self.n1_pos + self.pos

        distance = dist(electron_pos,photon.pos)

        if distance < 40:
            return True

    def excite(self):
        self.inteaction_frame = frame_count

        self.n0_occ = 0
        self.n1_occ = 1

    def de_excite(self):

        self.inteaction_frame = frame_count
        self.n0_occ = 1
        self.n1_occ = 0

        ran_x = random.randint(-100,100)
        ran_y = random.randint(-100,100)

        new_pos = Vector(ran_x,ran_y).normalize()*100+self.n0_pos/2+self.n1_pos/2
        photons.append(Photon(new_pos,Vector(ran_x,ran_y),self.n1 - self.n0 ))

    def stim_emis(self, photon):
        if photon.energy == self.n1 - self.n0:
            self.inteaction_frame = frame_count
            self.n0_occ = 1
            self.n1_occ = 0
            ran_y = random.randint(-15,15)
            photons.append(Photon(photon.pos + Vector(0,-30),photon.dir,self.n1 - self.n0 ))

class Photon:
    def __init__(self,pos,direc,energy):
        self.pos = pos
        self.dir = direc.normalize()
        self.energy = energy

        self.created = frame_count

    def show(self):
        velocity = 10
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


atom = Atom()
atoms = [atom]
phot = Photon(Vector(-400,300),Vector(1,0),100)
phot2 = Photon(Vector(-1400,200),Vector(1,0),100)
photons = [phot,phot2]

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    scale(1.2)

    #show atoms
    for a in atoms:
        a.show()

    # show photons
    for p in photons:
        p.show()

    # listen for photon in atom (should be all atoms i ground state)
    for a in atoms:
        for p in photons:
            if a.interaction(p):
                if a.n0_occ == 1:
                    photons.remove(p)
                    a.excite()
                elif a.n1_occ == 1:
                    a.stim_emis(p)

    # for all excited atoms randomly see if they should de-excite
    # for a in atoms:
    #     if a.n1_occ == 1:
    #         if random.randint(0,a.n1_ht) == 1:
    #             a.de_excite()
    saver()
    with push_style():
        alpha_in_out(30,100)
        Text("Stimulated emission",(0,420),size=50)
    with push_style():
        alpha_in_out(120,140)
        Text("(Stimulated absorption)",(0,250),size=30)
    if frame_count > frames:
        to_gif()
        exit()



run(frame_rate=30)
