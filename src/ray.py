from vec3 import *

class Ray:
    def __init__(self, origin=None, direction=None, time=0):
        self.orig = origin if origin is not None else Point3()
        self.dir = direction if direction is not None else Vec3()
        self.tm = time

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir
    
    def time(self):
        return self.tm

    def at(self, t):
        return self.orig + t * self.dir