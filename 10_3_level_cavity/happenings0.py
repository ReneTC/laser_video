from pymin import *

frames = 110
x_move =630
x_delta= 640

def setup():
    size(width, height)

atoms = []
photons = []

a11 = Atom3((-x_move,300))
p11 = Photon(Vector(-x_move-x_delta/2,300),Vector(1,0),15)
photons.append(p11)
atoms.append(a11)


a21 = Atom3((-x_move+x_delta,300))
p21 = Photon(Vector(-x_move+x_delta/2,300),Vector(1,0),35)
photons.append(p21)
atoms.append(a21)


a31 = Atom3((-x_move+2*x_delta,300))
a31.n0_occ = 0
a31.n2_occ = 1
atoms.append(a31)


# - - - - - - - -
a12 = Atom3((-x_move,-390+180))
a12.n0_occ = 0
a12.n1_occ = 1
atoms.append(a12)
p12 = Photon(Vector(-x_move-x_delta/2,-390+180),Vector(1,0),15)
photons.append(p12)

a22 = Atom3((-x_move+x_delta,-390+180))
a22.n0_occ = 0
a22.n2_occ = 1
atoms.append(a22)
p22 = Photon(Vector(-x_move+x_delta/2,-390+180),Vector(1,0),35)
photons.append(p22)

a32 = Atom3((-x_move+2*x_delta,-390+180))
a32.n0_occ = 0
a32.n1_occ = 1
atoms.append(a32)

def sq(col):
    fill(col)
    rect((-width/2, height/2), width/3, -height/2)

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    no_stroke()

    with push_matrix():
        translate(0,0)
        sq(240)
        translate(width/3,0)
        sq(255)
        translate(width/3,0)
        sq(240)
        translate(width/3,0)
        sq(255)
    with push_matrix():
        translate(0,-536)
        sq(255)
        translate(width/3,0)
        sq(240)
        # translate(width/4,0)
        # sq(255)
        # translate(width/4,0)
        # sq(240)

    fill(0)
    stroke(0)
    Text("1 -> 2 Absorption",(-x_move,100),size =30)
    Text("1 -> 3 Absorption",(-x_move+x_delta,100),size =30)
    Text("Radiationless transition 3 -> 2",(-x_move+2*x_delta,120),size =30)
    Text("(very fast)",(-x_move+2*x_delta,80),size =30)
    Text("(spontaneous emssion rare)",(-x_move+2*x_delta,80-100-390),size =30)
    Text("Meta stable 2 -> 1",(-x_move+2*x_delta,120-100-390),size =30)
    Text("1 -> 2 Stimulated emission",(-x_move,-390),size =30)
    Text("1 -> 3 Stimulated emission",(-x_move+x_delta,-390),size =30)
    # Text("...",(-x_move+2*x_delta,-390),size =30)
    # Text("...",(-x_move+3*x_delta,-390),size =30)


    for a in atoms:
        a.show()
    for p in photons:
        p.show()

    # listen for photn atom intercation
    for a in atoms:
        for p in photons:
            if a.interaction(p) and frame_count > 5 + a.inteaction_frame:
                if a.n0_occ == 1:
                    a.excite(p)
                    photons.remove(p)
                elif a.n1_occ == 1:
                    if p.energy == 15:
                        a.stim_emis(p,photons)
                elif a.n2_occ == 1:
                    if p.energy == 35:
                        a.stim_emis(p,photons)

    if frame_count == 30:
        a31.n1_occ = 1
        a31.n2_occ = 0
    if frame_count == 50:
        a32.de_excite_2_1(photons)

    with push_style():
        alpha_out(0,color=(255,255,255))
        square((0,0),2000, mode='CENTER')
    with push_style():
        alpha_in(90-4,color=(255,255,255))
        square((0,0),2000, mode='CENTER')
    saver()
    if frame_count > frames:
        to_gif()
        exit()

run()
