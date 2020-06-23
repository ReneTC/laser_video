from pymin import *

frames = 80


def plotter():

    steps = 80
    length = 200
    values = np.linspace(0,length,steps)

    test = np.sin(values/100)*100

    with push_matrix():


        for i in range(0,steps):
            if i==(steps-1):
                return
            line((values[i],test[i]),(values[i+1],test[i+1]))
def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    background(255)
    stroke_weight(5)
    fill(0)
    plotter()


    if frame_count > frames:
        exit()

if __name__ == '__main__':
    run(frame_rate=30)
