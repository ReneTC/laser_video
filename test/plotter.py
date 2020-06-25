from pymin import *

frames = 80


def plotter():

    steps = frames
    length = 700
    values = np.linspace(0,length,steps)

    test = np.abs(np.sin(values/100+frame_count/10)*100)


    for i in range(0,frame_count):
        if i==(steps-1):
            return
        line((values[i],test[i]),(values[i+1],test[i+1]))


    arrow(Vector(0,0),Vector(700,0))
    arrow(Vector(0,0),Vector(0,250))
    Text("0",(-40,30),size=30, font = "i")
    Text("0.5",(-40,250/2),size=30, font = "i")
    Text("1",(-40,250-30),size=30, font = "i")
    Text("Excited",(-40,300),size=30, font = "b")
    Text("Time",(700,-30),size=30, font = "b")

def setup():
    size(width, height)

def draw():
    translate(width/2,height/2)
    scale(1,-1)
    background(255)
    # draw_grid()
    stroke_weight(5)
    fill(0)
    plotter()


    if frame_count > frames:
        exit()

if __name__ == '__main__':
    run(frame_rate=30)
