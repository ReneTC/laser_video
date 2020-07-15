from pymin import *
import random

frames = 270

def setup():
    size(width, height)

atoms = []
photons1 = []
photons2 = []
photons3 = []

dy = 350-10
for i in range(0,3):
    phot1 = Photon(Vector(600,dy+8*i),Vector(-1,0),15)
    photons1.append(phot1)
for i in range(0,50):
    test = Atom((-690+i*20,dy+10))
    if random.randint(0,100) < 25:
        test.n0_occ = 0
        test.n1_occ = 1
    atoms.append(test)

dy = 0-10
for i in range(0,3):
    phot1 = Photon(Vector(600,dy+8*i),Vector(-1,0),15)
    photons2.append(phot1)
for i in range(0,50):
    test = Atom((-690+i*20,dy+10))
    if random.randint(0,100) < 50:
        test.n0_occ = 0
        test.n1_occ = 1
    atoms.append(test)
dy = -350-10
for i in range(0,3):
    phot1 = Photon(Vector(600,dy+8*i),Vector(-1,0),15)
    photons3.append(phot1)
for i in range(0,50):
    test = Atom((-690+i*20,dy+10))
    if random.randint(0,100) < 80:
        test.n0_occ = 0
        test.n1_occ = 1
    atoms.append(test)

def draw():
    fps_counter()
    translate(width/2,height/2)

    background(255)
    scale(1,-1)
    stroke(0)
    stroke_weight(4)
    fill(0)
    with push_matrix():
        translate(0,350)
        Text("25 % excited",(0,100),size=30,font="b")
        Text("Photon gets eaten",(0,70),size=30,font="i")
        Text("Photons = " + str(len(photons1)),(0,-30),size=30,font="i")

    with push_matrix():
        translate(0,-350)
        Text("90 % excited",(0,100),size=30,font="b")
        Text("Photons are multiplied",(0,70),size=30,font="i")
        Text("Photons = " + str(len(photons3)),(0,-30),size=30,font="i")

    fill(240)
    rect((-width/2, height/3-150), width, -height/3)
    with push_matrix():
        translate(0,0)
        fill(0)
        Text("50 % excited",(0,100),size=30,font="b")
        Text("Number of photons is constant",(0,70),size=30,font="i")
        Text("Photons = " + str(len(photons2)),(0,-30),size=30,font="i")
    #show all atoms
    for a in atoms:
        a.show()

    for p in reversed(photons1):
        p.show()
    for p in reversed(photons2):
        p.show()
    for p in reversed(photons3):
        p.show()
        # if p.pos[0] > 700:
        #     p.dir[0] = -1*p.dir[0]
        # elif p.pos[0] < -700:
        #     p.dir[0] = -1*p.dir[0]
        # elif p.pos[1] > 250-15 or p.pos[1] < - 250+10:
        #     photons.remove(p)

    # listen for photn atom intercation
    for a in atoms:
        for p in photons1:
            if a.interaction(p) and frame_count > 15 + a.inteaction_frame:
                if a.n0_occ == 1:
                    photons1.remove(p)
                    a.excite()
                elif a.n1_occ == 1:
                    a.stim_emis(p,photons1)
        for p in photons2:
            if a.interaction(p) and frame_count > 15 + a.inteaction_frame:
                if a.n0_occ == 1:
                    photons2.remove(p)
                    a.excite()
                elif a.n1_occ == 1:
                    a.stim_emis(p,photons2)
        for p in photons3:
            if a.interaction(p) and frame_count > 15 + a.inteaction_frame:
                if a.n0_occ == 1:
                    photons3.remove(p)
                    a.excite()
                elif a.n1_occ == 1:
                    a.stim_emis(p,photons3)

DK


    saver()
    if frame_count > frames:
        exit()

to_gif()
# run(frame_rate=30)
