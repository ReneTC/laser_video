from pymin import *

frames = 80




def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    scale(1,-1)
    background(255)
    # draw_grid()
    stroke_weight(5)
    fill(0)
    values = np.linspace(0,200,frames)
    test = np.abs(np.sin(values/100+frame_count/10)*100)
    plotter(test)


    if frame_count > frames:
        exit()

if __name__ == '__main__':
    run(frame_rate=30)
