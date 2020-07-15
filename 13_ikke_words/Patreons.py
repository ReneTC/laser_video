from pymin import *

frames = 150

def setup():
    size(width, height)

words = ["L. ", "A. ", "B. ", "S. ", "E. ", "O. ", "R. "]
words_full = ["Sven Ostertag", "Bjartur Mortensen", "Kale Crosbie","Martin Vasilev", "Hendrick McDonald","1x Anonymous"]

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)

    translate(interpolate(0,1400,120),0)
    fill(0,0,0)
    alpha_in_out(0,999)
    Text("Supporters",(0,500),size = 150, align = "CENTER")
    for i in range(0,len(words_full)):
        translate(interpolate(0,(i+1)*300,120),0)
        fill(0,0,0)
        with push_style():
            alpha_in_out(3+4*i,999)
            Text(words_full[i],(0,250-i*100),size = 70, align = "CENTER",font = "i")

    saver()
    if frame_count > frames:
        exit()



run()
