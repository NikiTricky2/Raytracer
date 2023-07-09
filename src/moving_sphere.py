from constants import *
from vec3 import *
from ray import *
from hittable import *
from material import *

class MovingSphere(Hittable):
    def __init__(self, cen0: Point3, cen1: Point3, _time0: float, _time1: float, r: float, m: Material):
        self.center0 = cen0
        self.center1 = cen1
        self.time0 = _time0
        self.time1 = _time1
        self.radius = r
        self.mat = m
    
    def hit(self, r: Ray, t_min: float, t_max: float) -> tuple[bool, HitRecord]:
        rec = HitRecord()

        oc = r.origin() - self.center(r.time())
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
        outward_normal = (rec.p - self.center(r.time())) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.mat = self.mat

        return True, rec

    def center(self, time: float) -> float:
        return self.center0 + ((time - self.time0) / (self.time1 - self.time0)) * (self.center1 - self.center0)