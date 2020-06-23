import random
import numpy as np
from p5 import *
def get_ran_dir():
    no_dir = 11
    directions = np.linspace(0,360,no_dir)
    ran_no = random.randint(0,no_dir-1)
    ran_angle = np.radians(directions[ran_no])
    ran_x = sin(ran_angle)
    ran_y = cos(ran_angle)
    return Vector(ran_x,ran_y).normalize()
print(get_ran_dir())
