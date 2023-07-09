from constants import *
from ray import *
from vec3 import *
from hittable import *
from typing import Optional

class Material:
    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color, bool]:
        raise NotImplementedError("scatter method is not implemented in the derived class")
    
class Lambertian(Material):
    def __init__(self, color: Optional[Color] = Color()) -> None:
        self.albedo = color

    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color, bool]:
        scatter_direction = rec.normal + random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction, r_in.time())
        attenuation = self.albedo

        return scattered, attenuation, True

class Metal(Material):
    def __init__(self, color: Optional[Color] = Color(), fuzz: float = 1):
        self.albedo = color
        self.fuzz = fuzz if fuzz < 1 else 1

    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color, bool]:
        reflected = reflect(unit_vector(r_in.direction()), rec.normal)
        scattered = Ray(rec.p, reflected + self.fuzz*random_in_unit_sphere(), r_in.time())
        attenuation = self.albedo
        return scattered, attenuation, dot(scattered.direction(), rec.normal) > 0

class Dielectric(Material):
    def __init__(self, index_of_refraction: float):
        self.ir = index_of_refraction
    
    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color, bool]:
        attenuation = Color(1, 1, 1)
        refraction_ratio = 1/self.ir if rec.front_face else self.ir

        unit_direction = unit_vector(r_in.direction())
        cos_theta = min(dot(-unit_direction, rec.normal), 1)
        sin_theta = math.sqrt(1 - cos_theta**2)

        cannot_refract = (refraction_ratio * sin_theta) > 1
        if cannot_refract or self._reflectance(cos_theta, refraction_ratio) > random():
            direction = reflect(unit_direction, rec.normal)
        else:
            direction = refract(unit_direction, rec.normal, refraction_ratio)

        scattered = Ray(rec.p, direction, r_in.time())
        return scattered, attenuation, True
    
    def _reflectance(self, cosine: float, ref_idx: float):
        # Use Shlick's approximation for reference
        r0 = (1-ref_idx) / (1+ref_idx)
        r0 = r0**2
        return r0 + (1-r0)*pow((1 - cosine), 5)