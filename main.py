from vec3 import *
from ray import *
from color import *

import math

def hit_sphere(center, radius, r):
    oc = r.origin() - center
    a = r.direction().length_squared()
    half_b = dot(oc, r.direction())
    c = oc.length_squared() - radius**2
    discriminant = half_b**2 - a*c

    if discriminant < 0:
        return -1
    else:
        return (-half_b - math.sqrt(discriminant)) / a

def ray_color(r):
    t = hit_sphere(Point3(0, 0, -1), 0.5, r)
    if t > 0:
        N = unit_vector(r.at(t) - Vec3(0, 0, -1))
        return 0.5*Color(N.x()+1, N.y()+1, N.z()+1)
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1)
    return (1 - t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)

# Image
ASPECT_RATIO = 16 / 9
IMAGE_WIDTH = 400
IMAGE_HEIGHT = int(IMAGE_WIDTH / ASPECT_RATIO)

# Camera

viewport_height = 2
viewport_width = ASPECT_RATIO * viewport_height
focal_length = 1

origin = Point3(0, 0, 0)
horizontal = Vec3(viewport_width, 0, 0)
vertical = Vec3(0, viewport_height, 0)
lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3(0, 0, focal_length)

OUTFILE = "result.ppm"
f = open(OUTFILE, "w+")

f.write(f"P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n")

for j in range(IMAGE_HEIGHT, 0, -1):
    print("Scanlines remaining:", j, f"({int(100 * (1 - (j-1)/IMAGE_HEIGHT))}%)")
    for i in range(0, IMAGE_WIDTH, 1):
        u = i / (IMAGE_WIDTH - 1)
        v = j / (IMAGE_HEIGHT - 1)
        r = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
        pixel_color = ray_color(r)
        write_color(f, pixel_color)

print("Done.")
f.close()