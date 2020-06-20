import random
import numpy as np

no_dir = 10
directions = np.linspace(0,360,no_dir)
ran_no = random.randint(0,no_dir-1)
ran_angle = np.radians(directions[ran_no])

ran_x = np.sin(ran_angle)
ran_y = np.cos(ran_angle)

print(ran_x,ran_y)


180/(2*np.pi)
