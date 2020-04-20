import random

a = int(input())
b = [1, 2, 3]
while a > 0:
    ii = random.choice(b)
    print(ii)
    if ii > 3 or ii > a:
        print(a)
    elif a - ii == 0:
        print("Ты победил")
    else:
        a -= ii
        print(a)
    a1 = int(input())
    if a1 > 3 or a1 < 1 or a1 > a:
        print(a)
    elif a - a1 == 0:
        print("ИИ выйграл")
    else:
        a -= a1
        print(a)
