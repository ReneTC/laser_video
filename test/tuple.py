import random
import numpy as np

no_dir = 36

directions = np.linspace(0,360-360/no_dir,no_dir)
ran_no = random.randint(0,no_dir-1)
ran_angle = np.radians(directions[ran_no])
