x = 0
y = 0
n = 0
flag = True
cl_x = int(input())
cl_y = int(input())
stop = input()
kol = int(input())
while stop != 'стоп':
    if cl_x == x and cl_y == y:
        flag = False
    if stop == 'север':
        y += kol
        if flag:
            n += 1
    elif stop == 'запад':
        x -= kol
        if flag:
            n += 1
    elif stop == 'юг':
        y -= kol
        if flag:
            n += 1
    elif stop == 'восток':
        x += kol
        if flag:
            n += 1
    stop = input()
    if stop != 'стоп':
        kol = int(input())
print(n)
