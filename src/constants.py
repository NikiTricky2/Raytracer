import math
from random import random

# Constants

INFINITY = math.inf
PI = 3.1415926535897932385

# Utility functions

def degrees_to_radians(degrees: float) -> float:
    return degrees * PI / 180

def randbetween(min: float, max: float) -> float:
    return min + (max - min) * random()

def clamp(x: float, min: float, max: float) -> float:
    if x < min: return min
    if x > max: return max
    return x