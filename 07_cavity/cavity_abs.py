from pymin import *
import random

frames = 190

def setup():
    size(width, height)

atoms = []
photons = []
for i in range(0,10):
    atoms.append(Atom((-650+i*140,0)))

strope = Strope()

def draw():
    fps_counter()
    translate(width/2,height/2)

    background(255)
    scale(1,-1)
    stroke(0)
    stroke_weight(4)
    draw_box()
    strope.show()


    # flash and randomly excite
    if frame_count == 30:
        strope.flash(atoms,photons)

    #show all atoms
    for a in atoms:
        a.show()

    #show all photons
    for p in photons:
        p.show()

    for p in photons:
        if p.pos[1] > 250-10 or p.pos[1] < - 250+10:
            photons.remove(p)
        elif p.pos[0] > 700 and p.pos[0] > 0:
            p.dir[0] = -1*p.dir[0]
        elif p.pos[0] < - 700 and p.pos[0] < 0:
            p.dir[0] = -1*p.dir[0]

    # check if photons should be destroid or bounced
    for p in photons:
        if p.pos[1] > 250-10 or p.pos[1] < - 250+10:
            photons.remove(p)
        if p.pos[0] > 700 or p.pos[0] < - 700:
            p.dir[0] = -1*p.dir[0]


    # for all excited atoms randomly see if they should de-excite
    for a in atoms:
        if a.n1_occ == 1:
            if random.randint(0,a.n1_ht) == 1:
                a.de_excite(photons)

    # saver()
    if frame_count > frames:
        exit()

run(frame_rate=30)
