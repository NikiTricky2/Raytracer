from constants import *

class Camera:
    def __init__(self, lookfrom, lookat, vup, vfov, aspect_ratio):
        theta = degrees_to_radians(vfov)
        h = math.tan(theta/2)
        viewport_height = 2 * h
        viewport_width = aspect_ratio * viewport_height

        w = unit_vector(lookfrom - lookat)
        u = unit_vector(cross(vup, w))
        v = cross(w, u)

        self.origin = lookfrom
        self.horizontal = viewport_width * u
        self.vertical = viewport_height * v
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - w
    
    def get_ray(self, s, t):
        return Ray(self.origin, self.lower_left_corner + s*self.horizontal + t*self.vertical - self.origin)