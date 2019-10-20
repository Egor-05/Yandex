one = int(input())
two = int(input())
three = int(input())
a = 0
b = 0
while 1:
    a = int(input())
    b = int(input())

    if a == 1:
        if one - b >= 0:
            one -= b
    elif a == 2:
        if two - b >= 0:
            two -= b
    else:
        if three - b >= 0:
            three -= b

    if one == 0 and two == 0 and three == 0:
        break

    print(one, two, three)
print(0, 0, 0)
