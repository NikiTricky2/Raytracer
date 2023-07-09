from hittable import *
from vec3 import *
from material import *

import math

class Sphere(Hittable):
    def __init__(self, cen: Point3, r: float, mat: Material) -> None:
        self.center = cen
        self.radius = r
        self.mat = mat
    
    def hit(self, r: Ray, t_min: float, t_max: float) -> tuple[bool, HitRecord]:
        rec = HitRecord()

        oc = r.origin() - self.center
        a = r.direction().length_squared()
        half_b = dot(oc, r.direction())
        c = oc.length_squared() - self.radius**2

        discriminant = half_b**2 - a*c
        if discriminant < 0: return False, rec
        sqrtd = math.sqrt(discriminant)

        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False, rec
        
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.mat = self.mat

        return True, rec