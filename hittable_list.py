from hittable import *

class HittableList(Hittable):
    def __init__(self):
        self.hittable_list = []
    
    def clear(self):
        self.hittable_list = []
    
    def add(self, object):
        self.hittable_list.append(object)
    
    def hit(self, r, t_min, t_max):
        rec = HitRecord()
        hit_anything = False

        for object in self.hittable_list:
            hit, temp_rec = object.hit(r, t_min, t_max)
            if hit:
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec
        
        return hit_anything, rec