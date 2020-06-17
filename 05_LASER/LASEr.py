from pymin import *

frames = 120

def setup():
    size(width, height)

words = ["L. ", "A. ", "B. ", "S. ", "E. ", "O. ", "R. "]
words_full = ["Light ", "Amplification ", "By ", "Stimulated ", "Emission ", "Of ", "Radiation "]
words2 = ["L. ", "A. ", "S. ", "E. ", "R. "]

def draw():
    translate(width/2,height/2)
    background(255)
    scale(1,-1)

    for i in range(0,len(words)):
        fill(0,0,0)
        with push_style():
            alpha_in_out(4*i,999)
            Text(words[i],(-500+i*120,400),size = 120)
    for i in range(0,len(words_full)):
        fill(0,0,0)
        with push_style():
            alpha_in_out(3+4*i,999)
            Text(words_full[i],(-500,-100-i*50),size = 50, align = "LEFT")
    # for i in range(0,len(words2)):
    #     with push_style():
    #         alpha_in_out(50+4*i,999)
    #         Text(words2[i],(-500+i*120,0),size = 120)


    if frame_count > frames:
        exit()



run()
