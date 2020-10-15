import numpy as np
from lab3ex1 import *
from math import cos, tan, pi, sqrt

a = 100 * g * (tan(np.radians(30)) ** 2)
a1 = (2 * (cos(pi / 3)) ** 2) * (1 - tan(np.radians(30)) * tan(pi / 3))

print(sqrt(a / a1))