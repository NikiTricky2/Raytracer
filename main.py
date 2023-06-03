from constants import *
from color import *
from hittable_list import *
from sphere import *
from camera import *

import math

def ray_color(r, world, depth):
    if depth <= 0:
        return Color(0, 0, 0)
    hit, rec = world.hit(r, 0, INFINITY)
    if hit:
        target = rec.p + rec.normal + random_unit_in_sphere()
        return 0.5 * ray_color(Ray(rec.p, target - rec.p), world, depth-1)
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1)
    return (1 - t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)

# Image
ASPECT_RATIO = 16 / 9
IMAGE_WIDTH = 400
IMAGE_HEIGHT = int(IMAGE_WIDTH / ASPECT_RATIO)
SAMPLES_PER_PIXEL = 50
MAX_DEPTH = 10

# World
world = HittableList()
world.add(Sphere(Point3(0, -100.5, -1), 100))
world.add(Sphere(Point3(0, 0, -1), 0.5))

# Camera
cam = Camera(ASPECT_RATIO)

OUTFILE = "result.ppm"
f = open(OUTFILE, "w+")

f.write(f"P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n")

for j in range(IMAGE_HEIGHT, 0, -1):
    print("Scanlines remaining:", j, f"({int(100 * (1 - (j-1)/IMAGE_HEIGHT))}%)")
    for i in range(0, IMAGE_WIDTH, 1):
        pixel_color = Color(0, 0, 0)
        for s in range(SAMPLES_PER_PIXEL):
            u = (i + random()) / (IMAGE_WIDTH - 1)
            v = (j + random()) / (IMAGE_HEIGHT - 1)
            r = cam.get_ray(u, v)
            pixel_color += ray_color(r, world, MAX_DEPTH)
        write_color(f, pixel_color, SAMPLES_PER_PIXEL)

print("Done.")
f.close()