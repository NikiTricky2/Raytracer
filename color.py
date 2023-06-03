from vec3 import *

def write_color(out, pixel_color):
    # Write the translated [0,255] value of each color component.
    r = int(255.999 * pixel_color.x())
    g = int(255.999 * pixel_color.y())
    b = int(255.999 * pixel_color.z())
    out.write(f"{r} {g} {b}\n")