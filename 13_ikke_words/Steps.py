from pymin import *
frames = 200


def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    with push_matrix():
        with push_style():
            translate(interpolate(0,-200,-50,duration=100),0)
            fill(interpolate(255,0,0,duration=10))
            Text("1. continuously excite the atoms with the pump",(200,300),size=40, font = "i")
    with push_matrix():
        with push_style():
            translate(interpolate(0,-200,-50,duration=100),0)
            fill(interpolate(255,0,0,duration=10))
            Text("2. Wait for one of the atoms to send out a photon orthogonal to the mirrors",(200,100),size=40, font = "i")
    with push_matrix():
        with push_style():
            translate(interpolate(0,-200,-50,duration=100),0)
            fill(interpolate(255,0,0,duration=10))
            Text("3. the photon will bounce around and create more photons by stimulated emission",(200,-100),size=40, font = "i")

    # fill(0)
    no_stroke()
    saver()
    if frame_count > frames:
        # to_gif()
        exit()
run()
