from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    x, y = im.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    pixels = im.load()
    for i in range(x):
        for j in range(y):
            g, b = pixels[i, j][1:]
            if i - delta >= 0:
                r = pixels[i - delta, j][0]
            else:
                r = pixels[i, j][0]
            pixels2[i, j] = r, g, b
    res.save("res.jpg")


makeanagliph("image.jpg", 10)
