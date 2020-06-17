from pymin import *
import random

frames = 130
class Atom:
    def __init__(self):
        self.pos = Vector(0,0)
        self.excited = 0

        self.n0 = 200
        self.n1 = 300

        self.n1_ht = 30

        self.n0_pos = Vector(0,self.n0)
        self.n1_pos = Vector(0,self.n1)

        self.inteaction_frame = -20

        self.n0_occ = 1
        self.n1_occ = 0


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
        if self.excited != 0:
            return

        electron_pos = 0
        if self.excited == 0:
            electron_pos = self.n0_pos + self.pos
        if self.excited == 1:
            electron_pos = self.n1_pos + self.pos

        distance = dist(electron_pos,photon.pos)

        if distance < 40:
            return True

    def excite(self):
        if self.excited == 0:
            self.inteaction_frame = frame_count
            self.excited = 1

            self.n0_occ = 0
            self.n1_occ = 1

    def de_excite(self):
        if self.excited == 1:
            self.inteaction_frame = frame_count
            self.excited = 0
            self.n0_occ = 1
            self.n1_occ = 0

            ran_x = random.randint(-100,100)
            ran_y = random.randint(-100,100)

            new_pos = Vector(ran_x,ran_y).normalize()*100+self.n0_pos/2+self.n1_pos/2
            photons.append(Photon(new_pos,Vector(ran_x,ran_y)))




class Photon:
    def __init__(self,pos,direc,energy):
        self.pos = pos
        self.dir = direc.normalize()
        self.energy = energy

        self.created = frame_count

    def show(self):
        velocity = 15
        self.pos = self.pos + self.dir * velocity
        with push_matrix():
            translate(self.pos[0],self.pos[1])
            angle = atan2(self.dir[1], self.dir[0])
            rotate(angle)
            with push_style():
                alpha_c = interpolate(0,255,self.created,duration = 20)
                fill(0,0,0,alpha_c)
                stroke(0,0,0,alpha_c)
                stroke_weight(3)
                photon()


def setup():
    size(width, height)


atom = Atom()
atoms = [atom]
# phot = Photon(Vector(-400,-200),Vector(1,0),1)
photons = []

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
        pass
        # p.show()

    stroke(0)
    stroke_weight(3)
    stroke(100)
    with push_matrix():
        translate(interpolate(0,300,20),0)
        translate(interpolate(0,800,100),0)
        dist_shower((0,200),(0,300),5)
        with push_style():
            alpha_in_out(30,999)
            Text("2.00 eV", (70,270))
        with push_style():
            alpha_in_out(60,999)
            Text(" = ", (150,270))

        no_stroke()
        fill(235, 64, 52)
        translate(200,250)
        scale_in_out(70,999)
        square((0,0),50, mode = "CENTER")
    # saver()
    if frame_count > frames:
        exit()



# run(frame_rate=30)
to_gif()
