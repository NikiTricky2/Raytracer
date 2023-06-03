from constants import *

class Material:
    def scatter(self, r_in, rec, attenuation):
        raise NotImplementedError("scatter method is not implemented in the derived class")
    
class Lambertian(Material):
    def __init__(self, color=None):
        self.albedo = color if not color is None else Color()

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction)
        attenuation = self.albedo

        return scattered, attenuation, True

class Metal(Material):
    def __init__(self, color=None):
        self.albedo = color if not color is None else Color()

    def scatter(self, r_in, rec):
        reflected = reflect(unit_vector(r_in.direction()), rec.normal)
        scattered = Ray(rec.p, reflected)
        attenuation = self.albedo
        return scattered, attenuation, dot(scattered.direction(), rec.normal) > 0