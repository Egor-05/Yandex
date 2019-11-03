import random
chislo = 5
kuchy = []
for i in range(1, chislo + 1):
    kuchy.append(int(input('Исходное кол-во камней в ' + str(i) + ' куче: ')))
win = False  # False - ходит бот, True - ходит игрок
while any(i > 0 for i in kuchy):  # Проверка является ли хотя бы один элемент массива истиной,
    # если вместо any будет стоять all, то будет проверка являются ли все элементы массива истиной
    # проверку чей ход
    # ввод бота или игрока
    if win:
        a = int(input('Введите номер кучи: '))
        while (a < 1) or (a > chislo) or (kuchy[a - 1] == 0):
            a = int(input('Введите номер кучи заново: '))
        b = int(input('Введите количество камней: '))
        while b > kuchy[a - 1]:
            b = int(input('Введите количество камней заново: '))
        player = 'Игрок'
    else:
        a = random.randint(1, chislo)
        while kuchy[a - 1] == 0:
            a = random.randint(1, chislo)
        b = random.randint(1, kuchy[a - 1])
        player = 'Бот'
    # убирание камней из кучи
    print(player, ' взял ', b, 'камней из кучи', a)
    kuchy[a - 1] -= b
    # вывод оставшихся камней
    for i in range(1, chislo + 1):
        print('Осталось камней в куче', i, ' - ', kuchy[i - 1], end='. ')
    print()
    if all(i == 0 for i in kuchy):
        print(player + ' выйграл!')
    # изменение вводящего
    win = not win
