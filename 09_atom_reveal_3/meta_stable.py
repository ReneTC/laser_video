from pymin import *
import random

frames = 279
class Atom:
    def __init__(self):
        self.pos = Vector(0,0)
        self.excited = 0

        self.n0 = 200
        self.n1 = 300
        self.n2 = 425

        self.n1_ht = 26
        self.n2_ht = 15

        self.n0_pos = Vector(0,self.n0)
        self.n1_pos = Vector(0,self.n1)
        self.n2_pos = Vector(0,self.n2)

        self.inteaction_frame = -20

        self.n0_occ = 1
        self.n1_occ = 0
        self.n2_occ = 0


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
            stroke(200)
            fill(0,0,0,0)
            with push_matrix():
                circle(center,self.n0*2)
            with push_matrix():
                circle(center,self.n1*2)
            with push_matrix():
                circle(center,self.n2*2)

        with push_matrix():
            fill('#dadada')
            translate(0,self.n0)
            scale(self.n0_occ)
            # scale(interpolate(self.n1_occ,self.n0_occ,self.inteaction_frame,duration = 10))
            circle((0,0),50)
            fill(0)
            Text("e",(0,22,),size=30)

        with push_matrix():
            translate(0,self.n1)
            scale(self.n1_occ)
            # scale(interpolate(self.n0_occ,self.n1_occ,self.inteaction_frame,duration = 10))
            fill('#dadada')
            circle((0,0),50)
            fill(0)
            Text("e",(0,22,),size=30)

        with push_matrix():
            translate(0,self.n2)
            scale(self.n2_occ)
            # scale(interpolate(self.n0_occ,self.n2_occ,self.inteaction_frame,duration = 10))
            fill('#dadada')
            circle((0,0),50)
            fill(0)
            Text("e",(0,22,),size=30)



    def interaction(self, photon):
        # get electron pos
        if self.n1 - self.n0 != photon.energy and self.n2 - self.n0 != photon.energy:
            return
        electron_pos = 0
        if self.n0_occ == 1:
            electron_pos = self.n0_pos + self.pos
        elif self.n1_occ == 1:
            electron_pos = self.n1_pos + self.pos
        else:
            electron_pos = self.n2_pos + self.pos

        distance = dist(electron_pos,photon.pos)

        if distance < 40:
            return True

    def excite(self,photon):
        self.inteaction_frame = frame_count
        if self.n1 - self.n0 == photon.energy:
            self.n0_occ = 0
            self.n1_occ = 1
            self.n2_occ = 0
        if self.n2 - self.n0 == photon.energy:
            self.n0_occ = 0
            self.n1_occ = 0
            self.n2_occ = 1



    def de_excite_n1(self):

        self.inteaction_frame = frame_count
        self.n0_occ = 1
        self.n1_occ = 0
        self.n2_occ = 0

        ran_x = random.randint(-100,100)
        ran_y = random.randint(-100,100)

        new_pos = Vector(ran_x,ran_y).normalize()*100+self.n0_pos/2+self.n1_pos/2
        photons.append(Photon(new_pos,Vector(ran_x,ran_y),self.n1 - self.n0 ))

    def de_excite_n2(self):

        self.inteaction_frame = frame_count
        self.n0_occ = 0
        self.n1_occ = 1
        self.n2_occ = 0

        ran_x = random.randint(-100,100)
        ran_y = random.randint(-100,100)

        new_pos = Vector(ran_x,ran_y).normalize()*100+self.n0_pos/2+self.n2_pos/2
        # photons.append(Photon(new_pos,Vector(ran_x,ran_y),self.n2 - self.n1 ))



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
                if self.energy == 225:
                    col = (89,0,152)
                if self.energy == 125:
                    col = (66, 135, 245)
                alpha_c = interpolate(0,255,self.created,duration = 20)
                fill(*col,alpha_c)
                stroke(*col,alpha_c)
                stroke_weight(3)
                photon()


def setup():
    size(width, height)


atom = Atom()
atoms = [atom]
phot = Photon(Vector(-400,200),Vector(1,0),225)
phot2 = Photon(Vector(-2500*2/3,300),Vector(1,0),100)
photons = [phot,phot2]
phot3 = Photon(Vector(0,310),Vector(1,0),100)
phot4 = Photon(Vector(0,300-10),Vector(1,0),100)
photons2 = [phot3,phot4]
def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)

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
                photons.remove(p)
                a.excite(p)

    # for all excited atoms randomly see if they should de-excite
    for a in atoms:
        if a.n2_occ == 1:
            if random.randint(0,a.n2_ht) == 1:
                a.de_excite_n2()

    with push_style():
        alpha_in_out(0,40,color=(0,0,0))
        arrow(Vector(0,200),Vector(0,410))
        Text("Absorption from pump",(200,330),font="b")
    with push_style():
        alpha_in_out(40,110,color=(0,0,0))
        arrow(Vector(0,420),Vector(0,310))
        Text("Fast radiatonless transition",(-240,370),font="b")
    with push_style():
        alpha_in_out(110,170,color=(0,0,0))
        arrow(Vector(0,300),Vector(0,210))
        Text("Meta stabile state",(160,340))
        Text("Very long life time",(-220,270),font="b")
    a = 30
    with push_style():
        alpha_in_out(110,170,color=(0,0,0))
        Text("Wait for stimualted emis",(-220,270-a))
    fill(0)
    if frame_count > 165:
        atom.n1_occ = 0
        atom.n0_occ = 1


        for p in photons2:
            p.show()

    saver()
    if frame_count > frames:
        to_gif()
        exit()

run(frame_rate=30)
