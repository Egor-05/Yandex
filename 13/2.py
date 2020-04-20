c = 0
p1 = 1
p2 = 1
p3 = 1
p4 = p1 + p2 + p3
a = int(input())
if a == 1:
    print(p1)
    c += 1
elif a == 2:
    print(p1)
    c += 1
    print(p2)
    c += 1
else:
    print(p1)
    c += 1
    print(p2)
    c += 1
    print(p3)
    c += 1
while True:
    if a == 1:
        break
    elif a == 2:
        break
    elif a == 3:
        break
    print(p4)
    c += 1
    if c >= a:
        break
    p1 = p2
    p2 = p3
    p3 = p4
    p4 = p1 + p2 + p3
