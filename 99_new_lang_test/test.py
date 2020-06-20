from ProcessingQt import *

width = 1000
height = 750


def arrow(_from,to,colour = '#000000'):
    p1 = _from
    p2 = to
    offset = 20
    angle = atan2(p1.y-p2.y, p1.x-p2.x)

    # main line
    # stroke(colour)
    line(p1,p2)

    translate(p2.x, p2.y)
    rotate(angle-PI/2)
    triangle((-offset*0.5, offset),(offset*0.5, offset),(0.5,-offset/2))


def photon():

    steps = 80
    length = 200
    translate(-200,0)
    arrow(Vector(199,0),Vector(200,0))

    values = np.linspace(0,length,steps)

    def cost(y): #sinus function cos(t)
        #decay end of lie
        decay = 1
        decay_length = length-40
        if y > decay_length:
            Y = (y-decay_length)/(length-decay_length) * (0-7)
            decay = exp(Y)

        return cos(y/(2*PI)+frame_count/3)*20*decay

    for i in range(0,steps):
        if i==(steps-1):
            return
        line((values[i],cost(values[i])),(values[i+1],cost(values[i+1])))

def setup():
    size(width, height)



def draw():
    background(255)
    translate(width/2,height/2)
    scale(1,-1)

    fill(0)
    circle(0,0,250)
    photon()


run()
