from vec3 import *

class Ray:
    def __init__(self, origin=None, direction=None):
        self.orig = origin if origin is not None else Point3()
        self.dir = direction if direction is not None else Vec3()

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir

    def at(self, t):
        return self.orig + t * self.dir