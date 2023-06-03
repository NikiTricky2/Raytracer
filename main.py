from vec3 import *
from color import *

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256

OUTFILE = "result.ppm"
f = open(OUTFILE, "w+")

f.write(f"P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n")

for j in range(IMAGE_HEIGHT, 0, -1):
    print("Scanlines remaining:", j, f"({int(100 * (1 - (j-1)/IMAGE_HEIGHT))}%)")
    
    for i in range(0, IMAGE_WIDTH, 1):
        pixel_color = Color(i / (IMAGE_WIDTH - 1), j / (IMAGE_HEIGHT - 1), 0.25)
        write_color(f, pixel_color)

print("Done.")
f.close()