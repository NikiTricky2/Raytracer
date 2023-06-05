from vec3 import *

class HitRecord:
    def __init__(self, p=None, normal=None, t=0, mat_ptr=None):
        self.p = p if p is not None else Point3()
        self.normal = normal if normal is not None else Vec3()
        self.mat_ptr = mat_ptr if normal is not None else Color()
        self.t = t
    
    def set_face_normal(self, r, outward_normal):
        self.front_face = dot(r.direction(), outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class Hittable:
    def hit(self, r, t_min, t_max):
        raise NotImplementedError("hit method is not implemented in the derived class")