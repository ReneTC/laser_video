from pymin import *

frames = 150



class Atom:
    def __init__(self):
        self.pos = Vector(0,0)

        self.n0 = 0
        self.n1 = 20

        self.n1_ht = 15

        self.n0_pos = Vector(0,self.n0)
        self.n1_pos = Vector(0,self.n1)

        self.inteaction_frame = -20

        self.n0_occ = 1
        self.n1_occ = 0


    def show(self):
        no_stroke()

        center = Vector(0,0)
        # proton
        # energy levels circles
        with push_style():
            stroke_weight(3)
            stroke('#dadada')
            fill(0,0,0,0)
            with push_matrix():

                line((-30,self.n0),(30,self.n0))
            with push_matrix():
                line((-30,self.n1),(30,self.n1))

        with push_matrix():
            fill(0)
            translate(0,self.n0)
            scale(interpolate(self.n1_occ,self.n0_occ,self.inteaction_frame,duration = 10))
            circle((0,0),15)

        with push_matrix():
            translate(0,self.n1)
            scale(interpolate(self.n0_occ,self.n1_occ,self.inteaction_frame,duration = 10))
            fill(0)
            circle((0,0),15)



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


def setup():
    size(width, height)


atom = Atom()

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)

    stroke(0)
    stroke_weight(3)
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

    atom.show()
    if frame_count > frames:
        exit()

    # saver()

run()
# to_gif()
