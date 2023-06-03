from constants import *

def write_color(out, pixel_color, samples_per_pixel):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Divide the color by the number of samples
    scale = 1 / samples_per_pixel
    r *= scale
    g *= scale
    b *= scale

    # Write the translated [0,255] value of each color component.
    r = int(255 * clamp(r, 0, 0.999))
    g = int(255 * clamp(g, 0, 0.999))
    b = int(255 * clamp(b, 0, 0.999))
    out.write(f"{r} {g} {b}\n")