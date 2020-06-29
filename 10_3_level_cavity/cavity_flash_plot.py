from pymin import *
import random

frames = 220

def setup():
    size(width, height)

atoms = []
photons = []
for i in range(0,10):
    for j in range(0,10):
        atoms.append(Atom3((-630+i*140+random.randint(-50,50),j*40-175+random.randint(-30,30))))

excited_data = np.zeros(frames)
strope = Strope()
def draw():
    exc = 0
    fps_counter()
    translate(0,-50)
    translate(width/2,height/2)

    background(255)
    scale(1,-1)
    stroke(0)
    stroke_weight(4)
    draw_box()
    strope.show()

    if frame_count == 10:
        strope.flash(atoms,photons)
    if frame_count == 80:
        strope.flash(atoms,photons)
    if frame_count == 150:
        strope.flash(atoms,photons)

    #show all atoms
    for a in atoms:
        a.show()
        if a.n1_occ == 1:
            exc += 1


    for p in reversed(photons):
        p.show()
        if p.pos[0] > 700:
            p.dir[0] = -1*p.dir[0]
        elif p.pos[0] < -700:
            p.dir[0] = -1*p.dir[0]
        elif p.pos[1] > 250-15 or p.pos[1] < - 250+10:
            photons.remove(p)

    # listen for photn atom intercation
    for a in atoms:
        for p in photons:
            if a.interaction(p) and frame_count > 5 + a.inteaction_frame:
                if a.n0_occ == 1 and p.energy == 15:
                    a.excite(p)
                    photons.remove(p)
                elif a.n1_occ == 1:
                    if p.energy == 20:
                        a.excite(p)
                        photons.remove(p)
                    else:
                        a.stim_emis(p,photons)


    # for all excited atoms randomly see if they should de-excite
    for a in atoms:
        # if a.n1_occ == 1:
        #     if random.randint(0,a.n1_ht) == 1:
        #         a.de_excite_2_1(photons)
        if a.n2_occ == 1:
            if random.randint(0,a.n2_ht) == 1:
                a.de_excite_3_2(photons)


    # plot
    no_excited = exc/np.size(atoms)*200
    excited_data[frame_count] = no_excited
    translate(-350,-500)

    stroke_weight(5)
    plotter(excited_data)


    # saver()
    if frame_count > frames:
        # to_gif()
        exit()

run(frame_rate=30)