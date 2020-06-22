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

    for p in reversed(photons):
        p.show()
        if p.pos[0] > 700:
            p.dir[0] = -1*p.dir[0]
        elif p.pos[0] < -700:
            p.dir[0] = -1*p.dir[0]
        elif p.pos[1] > 250-15 or p.pos[1] < - 250+10:
            photons.remove(p)



    # for all excited atoms randomly see if they should de-excite
    for a in atoms:
        if a.n1_occ == 1:
            if random.randint(0,a.n1_ht) == 1:
                a.de_excite(photons)

    # saver()
    if frame_count > frames:
        # to_gif()
        exit()

run(frame_rate=30)
