import random
one = int(input('Исходное кол-во камней в первой куче: '))
two = int(input('Исходное кол-во камней во второй куче: '))
three = int(input('Исходное кол-во камней в третьей куче: '))
win = False  # False - ходит бот, True - ходит игрок
while one != 0 or two != 0 or three != 0:
    # проверку чей ход
    # ввод бота или игрока
    if win:
        a = int(input('Введите номер кучи: '))
        while (a == 1 and one == 0) or (a == 2 and two == 0) or (a == 3 and three == 0)\
                or (a < 1) or (a > 3):
            a = int(input('Введите номер кучи заново: '))
        b = int(input('Введите количество камней: '))
        while (a == 1 and b > one) or (a == 2 and b > two) or (a == 3 and b > three):
            b = int(input('Введите количество камней заново: '))
        player = 'Игрок'
    else:
        a = random.randint(1, 3)
        while (a == 1 and one == 0) or (a == 2 and two == 0) or (a == 3 and three == 0):
            a = random.randint(1, 3)
        if a == 1:
            b = random.randint(1, one)
        elif a == 2:
            b = random.randint(1, two)
        else:
            b = random.randint(1, three)
        player = 'Бот'
    # убирание камней из кучи
    print(player, ' взял ', b, 'камней из кучи', a)
    if a == 1:
        if b <= one:
            one -= b
    elif a == 2:
        if b <= two:
            two -= b
    else:
        if b <= three:
            three -= b
    # вывод оставшихся камней
    print('Осталось камней в первой куче', one, ', во второй -', two, ', в третьей -', three, '.')
    # проверка на победу
    if one == two == three == 0:
        print(player + ' выйграл!')
    # изменение вводящего
    win = not win
