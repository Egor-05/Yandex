import random
one = int(input('Исходное кол-во камней в первой куче: '))
two = int(input('Исходное кол-во камней во второй куче: '))
c = [1, 2, 3, 4, 5]
d = [1, 2]
while one != 0 and two != 0:
    ii = random.choice(d)
    iii = random.choice(c)
    print(ii)
    print(iii)

    if a == 1 and one - b == 0 and two == 0:
        print('Ты выйграл!!!')
    elif a == 2 and two - b == 0 and one == 0:
        print('Ты выйграл!!!')
    else:
        print('ИИ выйграл!!!')

    if ii == 1:
        if one - iii >= 0:
            one -= iii
    else:
        if two - iii >= 0:
            two -= iii
    print(one, two)

    a = int(input())
    b = int(input())
    while (a == 1 and b > one) or (a == 2 and b > two) or a != 1 or a != 2:
        if a == 1 and b > one:
            b = int(input('Введите число камней заново!'))
        elif a == 2 and b > two:
            b = int(input('Введите число камней заново!'))
        else:
            break

    if a == 1 and one - b == 0 and two == 0:
        print('Ты выйграл!!!')
    elif a == 2 and two - b == 0 and one == 0:
        print('Ты выйграл!!!')
    else:
        print('ИИ выйграл!!!')

    if a == 1:
        if one - b >= 0:
            one -= b
    else:
        if two - b >= 0:
            two -= b

    print(one, two)

print(0, 0)
