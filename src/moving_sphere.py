from constants import *
from vec3 import *
from ray import *
from hittable import *

class MovingSphere(Hittable):
    def __init__(self, cen0, cen1, _time0, _time1, r, m):
        self.center0 = cen0
        self.center1 = cen1
        self.time0 = _time0
        self.time1 = _time1
        self.radius = r
        self.mat_ptr = m
    
    def hit(self, r, t_min, t_max):
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
        rec.mat_ptr = self.mat_ptr

        return True, rec

    def center(self, time):
        return self.center0 + ((time - self.time0) / (self.time1 - self.time0)) * (self.center1 - self.center0)