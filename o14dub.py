from PIL import Image


def negative(s):
    s = Image.open(s)
    res = Image.new('RGB', s.size)
    x, y = s.size
    for i in range(x):
        for j in range(y):
            r, g, b = s.getpixel((i, j))
            res.putpixel((i, j), (255 - r, 255 - g, 255 - b))
    res.save('res.jpg', "JPEG")


negative('image.jpg')
