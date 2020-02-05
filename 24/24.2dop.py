import math


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def distance(t):
    return math.hypot(0.75 - t[0], 0 - t[1])


coords = [(math.cos(3 * t), math.sin(3 * t)) for t in drange(0, 2 * 3.14, 0.1)]
dists = [round(distance(x), 4) for x in coords]
print(min(dists))