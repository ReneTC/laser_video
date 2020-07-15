from pymin import *
frames = 10


def setup():
    size(width, height)

words = ["The ", "surprisingly ", "simple ", "physics ", "of ", "a ", "L.A.S.E.R "]
# words = ["Thecake", "b", "cd", "e"]
# words = ["The", "surprisingly"]
def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    # fill(interpolate(255,0,-7))
    fill(0)
    no_stroke()
    dx = -130
    if frame_count > 1:
        Text(words[0],(-500+dx,100),size=100,font="b")
    if frame_count > 2:
        nudge = 380
        Text(words[1],(-500+dx+nudge,100),size=100,font="i")
    if frame_count > 3:
        nudge = 380+450
        Text(words[2],(-500+dx+nudge,100),size=100,font="b")
    if frame_count > 4:
        nudge = 380+450+380
        Text(words[3],(-500+dx+nudge,100),size=100,font="b")
    dy = -120
    dx = - 220
    if frame_count > 5:
        Text(words[4],(-500+dx+370,100+dy),size=100,font="b")
    if frame_count > 6:
        nudge = 380+120
        Text(words[5],(-500+dx+nudge,100+dy),size=100,font="b")
    if frame_count > 7:
        nudge = 380+480
        Text(words[6],(-500+dx+nudge,100+dy),size=100,font="b")
    saver("start")
    if frame_count > frames:
        # to_gif()
        exit()
run()
