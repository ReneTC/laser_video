from pymin import *

frames = 250
size_x = 1920
size_y = 1080


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

    # flush_scene(150)
    text_align("CENTER")
    with push_style():
        alpha_in_out(0,150)
        stroke_weight(5)
        Text("E", (-620, 250),size=120)
        arrow(Vector(-500,-200),Vector(-500,200))
    time = 30
    stroke_weight(5)
    stroke(0)

    draw_line((-400,-150),(0,-150),time)
    draw_line((-400,-150+250),(0,-150+250),time+20)

    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(60,999)
        fill('#dadada')
        circle((0,0),70)
        fill(0)
        Text("e",(0,35),size=50)

    #n1
    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(60,999)
        fill(0)
        Text("n1",(250,35),size=50)

    #n2
    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(60,999)
        fill(0)
        Text("n2",(250,35+250),size=50)

    # how physisst.
    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(75,155)
        fill(0)
        Text("Normal representation of a two level atom",(0,630),size=50,font = "b")
    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(100,999)
        fill(0)
        Text("But let's change it to..",(0,550),size=50, font = "i")

    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(190,999)
        fill(0)
        Text("this! :)",(0,-220),size=50, font = "i")


    # grey circle
    with push_matrix():
        no_stroke()
        translate(-200,-150+250/2)
        scale_in_out(175,999)
        fill(240)
        circle((0,0),650)

    # grey lines
    with push_style():
        stroke(150)
        draw_line((-400,-150),(0,-150),170)
        draw_line((-400,-150+250),(0,-150+250),170)

    # black electron
    with push_matrix():
        no_stroke()
        translate(-200,-150)
        scale_in_out(160,999)
        fill(0)
        circle((0,0),70)
        fill(0)
    if frame_count == frames:
        exit()

    # saver()
run(frame_rate=30)
# to_gif()
