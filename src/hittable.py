from vec3 import *
from ray import *
from typing import Optional

class HitRecord:
    def __init__(self, p: Optional[Point3] = Point3(), normal: Optional[Vec3] = Vec3(), t: float = 0, mat: Optional[Color] = Color()) -> None:
        self.p = p
        self.normal = normal
        self.mat = mat
        self.t = t
    
    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        self.front_face = dot(r.direction(), outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class Hittable:
    def hit(self, r: Ray, t_min: float, t_max: float) -> tuple[bool, Ray]:
        raise NotImplementedError("hit method is not implemented in the derived class")