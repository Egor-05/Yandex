import random
one = int(input('Исходное кол-во камней в первой куче: '))
two = int(input('Исходное кол-во камней во второй куче: '))
three = int(input('Исходное кол-во камней в третьей куче: '))
c = [1, 2, 3, 4, 5]
d = [1, 2, 3]
while one != 0 and two != 0 and three != 0:
    ii = random.choice(d)
    iii = random.choice(c)
    print(ii)
    print(iii)

    if a == 1 and one - b == 0 and two == 0 and three == 0:
        print('Ты выйграл!!!')
    elif a == 2 and two - b == 0 and one == 0 and three == 0:
        print('Ты выйграл!!!')
    elif a == 3 and three - b == 0 and one == 0 and two == 0:
        print('Ты выйграл!!!')
    else:
        print('ИИ выйграл!!!')

    if ii == 1:
        if one - iii >= 0:
            one -= iii
    elif ii == 2:
        if two - iii >= 0:
            two -= iii
    else:
        if three - iii >= 0:
            three -= iii

    print(one, two, three)

    a = int(input())
    b = int(input())
    while (a == 1 and b > one) or (a == 2 and b > two) or a != 1 or a != 2:
        if a == 1 and b > one:
            b = int(input('Введите число камней заново!'))
        elif a == 2 and b > two:
            b = int(input('Введите число камней заново!'))
        elif a == 3 and b > three:
            b = int(input('Введите число камней заново!'))

    if a == 1 and one - b == 0 and two == 0 and three == 0:
        print('Ты выйграл!!!')
    elif a == 2 and two - b == 0 and one == 0 and three == 0:
        print('Ты выйграл!!!')
    elif a == 3 and three - b == 0 and one == 0 and two == 0:
        print('Ты выйграл!!!')
    else:
        print('ИИ выйграл!!!')

    if a == 1:
        if one - b >= 0:
            one -= b
    elif a == 2:
        if two - b >= 0:
            two -= b
    else:
        if three - b >= 0:
            three -= b

    print(one, two, three)
print(0, 0, 0)
