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

def random_scene():
    world = HittableList()

    ground_material = Lambertian(Color(0.5, 0.5, 0.5))
    world.add(Sphere(Point3(0, -1000, 0), 1000, ground_material))

    for a in range(-11, 11):
        for b in range(-11, 11):
            choose_mat = random()
            center = Point3(a + 0.9*random(), 0.2, b+0.9*random())

            if a == -4 and b == 0:
                material2 = Lambertian(Color(0.4, 0.2, 0.1))
                world.add(Sphere(Point3(-4, 1, 0), 1, material2))
            elif a == 0 and b == 0:
                material1 = Dielectric(1.5)
                world.add(Sphere(Point3(0, 1, 0), 1, material1))
            elif a == 4 and b == 0:
                material3 = Metal(Color(0.7, 0.6, 0.5), 0)
                world.add(Sphere(Point3(4, 1, 0), 1, material3))

            if (center - Point3(4, 0.2, 0)).length() > 0.9:
                if choose_mat < 0.8:
                    # diffuse
                    albedo = Color.random() * Color.random()
                    sphere_material = Lambertian(albedo)
                    world.add(Sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    # metal
                    albedo = Color.randbetween(0.5, 1)
                    fuzz = randbetween(0, 0.5)
                    world.add(Sphere(center, 0.2, sphere_material))
                else:
                    # glass
                    sphere_material = Dielectric(1.5)
                    world.add(Sphere(center, 0.2, sphere_material))

    return world

# Image
ASPECT_RATIO = 3 / 2
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = int(IMAGE_WIDTH / ASPECT_RATIO)
SAMPLES_PER_PIXEL = 100
MAX_DEPTH = 50

# World
world = random_scene()

# Camera
lookfrom = Point3(13, 2, 3)
lookat = Point3(0, 0, 0)
vup = Point3(0, 1, 0)
dist_to_focus = 10
aperture = 0.1

cam = Camera(lookfrom, lookat, vup, 20, ASPECT_RATIO, aperture, dist_to_focus)

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