from vec3 import *
from typing import Optional

class Ray:
    def __init__(self, origin: Optional[Point3] = Point3(), direction: Optional[Vec3] = Vec3(), time=0):
        self.orig = origin
        self.dir = direction
        self.tm = time

    def origin(self) -> float:
        return self.orig

    def direction(self) -> float:
        return self.dir
    
    def time(self) -> float:
        return self.tm

    def at(self, t: float) -> float:
        return self.orig + t * self.dir