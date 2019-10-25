import random
one = int(input('Исходное кол-во камней в первой куче: '))
two = int(input('Исходное кол-во камней во второй куче: '))
three = int(input('Исходное кол-во камней в третьей куче: '))
win = False # False - ходит бот, True - ходит игрок
c = [1, 2, 3, 4, 5]
d = [1, 2, 3]
while one != 0 and two != 0 and three != 0:
    # проверку чей ход
    if win:
        a = int(input('Введите номер кучи:'))
        b = int(input('Введите количество камней:'))
    else:
        a = random.randint(b)



    # ввод бота или игрока
    # проверка на победу
    # вывод оставшихся камней
    # изменение вводящего
    ii = random.choice(d)
    iii = random.choice(c)
    print(ii)
    print(iii)

    if ii == 1:
        if one - iii >= 0:
            one -= iii
    elif ii == 2:
        if two - iii >= 0:
            two -= iii
    else:
        if three - iii >= 0:
            three -= iii
    if (win is False) and one == 0 and two == 0 and three == 0:
        print('Бот выйграл!')
    print(one, two, three)

    win = not win

    a = int(input('Введите номер кучи: '))
    b = int(input('Введите количество камней которое вы хотите взять: '))
    while (a == 1 and b > one) or (a == 2 and b > two) or (a == 3 and b > three) or a != 1 or a != 2:
        if a == 1 and b > one:
            b = int(input('Введите число камней заново!'))
        elif a == 2 and b > two:
            b = int(input('Введите число камней заново!'))
        elif a == 3 and b > three:
            b = int(input('Введите число камней заново!'))

    if a == 1:
        if one - b >= 0:
            one -= b
    elif a == 2:
        if two - b >= 0:
            two -= b
    elif a == 3:
        if three - b >= 0:
            three -= b

    if (win is True) and one == 0 and two == 0 and three == 0:
        print('Игрок выйграл!')

    print(one, two, three)
    win = not win
print(0, 0, 0)
