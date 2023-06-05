import math
from random import random

# Constants

INFINITY = math.inf
PI = 3.1415926535897932385

# Utility functions

def degrees_to_radians(degrees):
    return degrees * PI / 180

def randbetween(min, max):
    return min + (max - min) * random()

def clamp(x, min, max):
    if x < min: return min
    if x > max: return max
    return x

# Common imports

from ray import *
from vec3 import *