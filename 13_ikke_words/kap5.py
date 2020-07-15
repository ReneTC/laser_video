from pymin import *
frames = 100


def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    with push_matrix():
        with push_style():
            translate(interpolate(255,0,-50,duration=100),0)
            translate(interpolate(0,-1200,60,duration=40),0)
            fill(interpolate(255,0,-50,duration=100))
            Text("Chapter 4",(-300,300),size=200,font="i")
    with push_matrix():
        with push_style():
            translate(interpolate(-255,0,-50,duration=100),0)
            translate(interpolate(0,1600,60,duration=40),0)
            fill(interpolate(255,0,0,duration=100))
            translate(0,0)
            fill(0)
            Text("A Working laser",(100,0),size=100, font = "i")
    with push_style():
        alpha_out(0,color=(255,255,255))
        square((0,0),2000, mode='CENTER')
    # fill(0)
    no_stroke()
    saver()
    if frame_count > frames:
        # to_gif()
        exit()
run()
