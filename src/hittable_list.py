from hittable import *
from ray import *

class HittableList(Hittable):
    def __init__(self):
        self.hittable_list = []
    
    def clear(self) -> None:
        self.hittable_list = []
    
    def add(self, object: Hittable) -> None:
        self.hittable_list.append(object)
    
    def hit(self, r: Ray, t_min: float, t_max: float) -> tuple[bool, HitRecord]:
        rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for object in self.hittable_list:
            hit, temp_rec = object.hit(r, t_min, t_max)
            if hit and temp_rec.t < closest_so_far:
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec
        
        return hit_anything, rec