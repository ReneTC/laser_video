from pymin import *

frames = 170
size_x = 1920
size_y = 1080


def arrow(p1,p2):
    offset = 40
    stroke_weight(8)

    # main line
    stroke(0)
    line(p1,p2)

    with push_matrix():
        no_stroke()
        angle = atan2(p1.y-p2.y, p1.x-p2.x)
        translate(p2.x, p2.y)
        rotate(angle-PI/2)
        triangle((-offset*0.5, offset),(offset*0.5, offset),(0,-offset/2))

def setup():
    size(size_x, size_y)
    latex = create_font("/home/renec/Drive/Higgsino/ASSETS/andet/font/cmunti.ttf", 120)
    text_font(latex)

def draw():
    background(255)
    translate(300,0)
    translate(width/2,height/2)
    background(255)
    scale(1,-1)
    in_scene(0)
    flush_scene(150)
    text_align("CENTER")
    fill(0)
    Text("E", (-620, 250),size=120)

    arrow(Vector(-500,-200),Vector(-500,200))

    stroke(0)
    stroke_weight(5)
    time = 30
    draw_line((-400,-150),(0,-150),time)
    draw_line((-400,-150+250),(0,-150+250),time+20)

    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(60,90)
        fill('#dadada')
        circle((0,0),70)
        fill(0)
        Text("e",(0,35),size=50)

    with push_matrix():
        no_stroke()
        translate(-200,-150+250)
        scale_in_out(90,130)
        fill('#dadada')
        circle((0,0),70)
        fill(0)
        Text("e",(0,35),size=50)


    if frame_count == frames:
        exit()

    saver()
run(frame_rate=30)
# to_gif()
