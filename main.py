from constants import *
from color import *
from hittable_list import *
from sphere import *
from camera import *
from material import *

import math

def ray_color(r, world, depth):
    if depth <= 0:
        return Color(0, 0, 0)
    
    hit, rec = world.hit(r, 0.001, INFINITY)
    if hit:
        scattered, attenuation, res = rec.mat_ptr.scatter(r, rec)
        if res:
            return attenuation * ray_color(scattered, world, depth-1)
        return Color(0, 0, 0)
    
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1)
    return (1 - t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)

# Image
ASPECT_RATIO = 16 / 9
IMAGE_WIDTH = 400
IMAGE_HEIGHT = int(IMAGE_WIDTH / ASPECT_RATIO)
SAMPLES_PER_PIXEL = 10
MAX_DEPTH = 20

# World

R = math.cos(PI/4)
world = HittableList()

material_left = Lambertian(Color(0,0,1))
material_right = Lambertian(Color(1,0,0))

world.add(Sphere(Point3(-R, 0, -1), R, material_left))
world.add(Sphere(Point3(R, 0, -1), R, material_right))

# Camera
cam = Camera(90, ASPECT_RATIO)

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