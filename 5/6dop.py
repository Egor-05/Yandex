import random
one = int(input('Исходное кол-во камней в первой куче: '))
two = int(input('Исходное кол-во камней во второй куче: '))
win = False  # False - ходит бот, True - ходит игрок
while one != 0 or two != 0:
    # проверка чей ход
    # ввод бота или игрока
    if win:
        a = int(input('Введите номер кучи: '))
        while (a == 1 and one == 0) or (a == 2 and two == 0) or (a < 1) or (a > 2):
            a = int(input('Введите номер кучи заново: '))
        b = int(input('Введите количество камней: '))
        while (a == 1 and b > one) or (a == 2 and b > two):
            b = int(input('Введите количество камней заново: '))
        player = 'Игрок'
    else:
        a = random.randint(1, 3)
        while (a == 1 and one == 0) or (a == 2 and two == 0):
            a = random.randint(1, 2)
        if a == 1:
            b = random.randint(1, one)
        elif a == 2:
            b = random.randint(1, two)
        player = 'Бот'
    # убирание камней из кучи
    print(player, ' взял ', b, 'камней из кучи', a)
    if a == 1:
        if b <= one:
            one -= b
    elif a == 2:
        if b <= two:
            two -= b
    # вывод оставшихся камней
    print('Осталось камней в первой куче', one, ', во второй куче ', two, '.')
    # проверка на победу
    if one == two == 0:
        print(player + ' выйграл!')
    # изменение вводящего
    win = not win
