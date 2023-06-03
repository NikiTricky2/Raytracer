IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256

OUTFILE = "result.ppm"
f = open(OUTFILE, "w+")

f.write(f"P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n")

for j in range(IMAGE_HEIGHT, 0, -1):
    for i in range(0, IMAGE_WIDTH, 1):
        r = i / (IMAGE_WIDTH - 1)
        g = j / (IMAGE_HEIGHT - 1)
        b = 0.25

        ir = int(255.999 * r)
        ig = int(255.999 * g)
        ib = int(255.999 * b)

        f.write(f"{ir} {ig} {ib}\n")

f.close()