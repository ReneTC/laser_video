from pymin import *
import random

frames = 190

def setup():
    size(width, height)

atoms = []
photons = []
for i in range(0,10):
    atoms.append(Atom((-650+i*140,random.randint(-200,200))))

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
    if frame_count %30 == 0:
        strope.flash(atoms,photons)

    #show all atoms
    for a in atoms:
        a.show()

    #show all atoms
    for p in photons:
        p.show()

    # for all excited atoms randomly see if they should de-excite
    for a in atoms:
        if a.n1_occ == 1:
            if random.randint(0,a.n1_ht) == 1:
                a.de_excite(photons)

    if frame_count > frames:
        exit()

run(frame_rate=30)
