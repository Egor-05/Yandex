last = 0
f = 0
s = 0
maxx = 1
while 1:
    x = int(input())
    if x == 0:
        break
    else:
        if maxx == 1:
            if x * last % 7 == 0 and x * last % 49 != 0 and x * last > maxx:
                maxx = x * last
                f = x
                s = last
        else:
            if x * f % 7 == 0 and x * f % 49 != 0 and x * f > maxx:
                maxx = x * f
                s = x
            if x * s % 7 == 0 and x * s % 49 != 0 and x * s > maxx:
                maxx = x * s
                f = x
    last = x
print(maxx)