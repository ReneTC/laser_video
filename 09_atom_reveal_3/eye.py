from pymin import *
import random

frames = 279

def setup():
    size(width, height)


def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    translate(-200,200)
    with push_style():
        stroke_weight(3)
        fill(235, 64, 52)
        stroke(235, 64, 52)
        photon()
        Text("2.00 eV - visible",(300,20),font="b")
        alpha_out(60,color=(255,255,255))
        square((0,0),2000, mode='CENTER')

    translate(0,-200)
    with push_style():
        stroke_weight(3)
        fill(66, 135, 245)
        stroke(66, 135, 245)
        photon()
        Text("3.00 eV - visible",(300,20),font="b")
        alpha_out(30,color=(255,255,255))
        square((0,0),2000, mode='CENTER')

    translate(0,-200)
    with push_style():
        stroke_weight(3)
        fill(89,0,152)
        stroke(89,0,152)
        photon()
        Text("5.00 eV - not visible",(300,20),font="b")
        alpha_out(0,color=(255,255,255))
        square((0,0),2000, mode='CENTER')
    saver()
    if frame_count > frames:
        # to_gif()
        exit()

run(frame_rate=30)
