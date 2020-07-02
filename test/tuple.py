import numpy as np
import random

no_dir = 17
directions = np.linspace(0,360,no_dir)

ran_no = random.randint(0,no_dir-1)
ran_angle = np.radians(directions[ran_no])
ran_angle = np.pi/2
ran_x = np.sin(ran_angle)
ran_y = np.cos(ran_angle)

print(ran_x,ran_y)
