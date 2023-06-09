from constants import *
from ray import *
from vec3 import *

class Camera:
    def __init__(self, lookfrom, lookat, vup, vfov, aspect_ratio, aperture, focus_dist, _time0=0, _time1=0):
        theta = degrees_to_radians(vfov)
        h = math.tan(theta/2)
        viewport_height = 2 * h
        viewport_width = aspect_ratio * viewport_height

        self.w = unit_vector(lookfrom - lookat)
        self.u = unit_vector(cross(vup, self.w))
        self.v = cross(self.w, self.u)

        self.origin = lookfrom
        self.horizontal = focus_dist * viewport_width * self.u
        self.vertical = focus_dist * viewport_height * self.v
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - focus_dist * self.w

        self.lens_radius = aperture / 2

        # Shutter open/close times
        self.time0 = _time0
        self.time1 = _time1
    
    def get_ray(self, s, t):
        rd = self.lens_radius * random_in_unit_disk()
        offset = self.u * rd.x() + self.v * rd.y()

        return Ray(
            self.origin + offset, 
            self.lower_left_corner + s*self.horizontal + t*self.vertical - self.origin - offset,
            randbetween(self.time0, self.time1)
        )