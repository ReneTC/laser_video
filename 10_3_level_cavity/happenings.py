from pymin import *

frames = 150


def setup():
    size(width, height)

atoms = []
photons = []

a11 = Atom3((-730,300))
atoms.append(a11)


a21 = Atom3((-730+490,300))
atoms.append(a21)


a31 = Atom3((-730+2*490,300))
atoms.append(a31)


a41 = Atom3((-730+3*490,300))
atoms.append(a41)

# - - - - - - - -
a12 = Atom3((-730,-390+180))
atoms.append(a12)

a22 = Atom3((-730+490,-390+180))
atoms.append(a22)

a32 = Atom3((-730+2*490,-390+180))
atoms.append(a32)

a42 = Atom3((-730+3*490,-390+180))
atoms.append(a42)
def sq(col,txt):
    fill(0)

    fill(col)
    rect((-width/2, height/2), width/4, -height/2)

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    no_stroke()

    with push_matrix():
        translate(0,0)
        sq(240,"lol")
        translate(width/4,0)
        sq(255,"lol")
        translate(width/4,0)
        sq(240,"lol")
        translate(width/4,0)
        sq(255,"lol")
    with push_matrix():
        translate(0,-536)
        sq(255,"lol")
        translate(width/4,0)
        sq(240,"lol")
        translate(width/4,0)
        sq(255,"lol")
        translate(width/4,0)
        sq(240,"lol")

    fill(0)
    stroke(0)
    Text("The cake is a lie",(-730,100),size =50)
    Text("cake",(-730,-390),size =50)
    Text("lol wut",(-730+490,100),size =50)
    Text("hej",(-730+490,-390),size =50)
    Text("Hvad så der",(-730+2*490,100),size =50)
    Text("ej hvad",(-730+2*490,-390),size =50)
    Text("god aften far",(-730+3*490,100),size =50)
    Text("ko",(-730+3*490,-390),size =50)


    for a in atoms:
        a.show()
    if frame_count > frames:
        exit()

run()
