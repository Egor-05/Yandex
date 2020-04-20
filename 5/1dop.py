one = int(input())
two = int(input())
a = 0
b = 0
while 1:
    a = int(input())
    b = int(input())
    if a == 1:
        if one - b >= 0:
            one -= b
    else:
        if two - b >= 0:
            two -= b
    if one == 0 and two == 0:
        break
    print(one, two)
print(0, 0)
