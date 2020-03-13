import math

minn = round(math.hypot(0.75 - 1, 0), 4)
for i in range(0, 62, 1):
    minn = min(minn, round(math.hypot(0.75 - math.cos(3 * (i / 10)), 0 - math.sin(3 * (i / 10))), 4))
print(minn)
