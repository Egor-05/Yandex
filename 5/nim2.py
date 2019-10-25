import random
one = int(input('Исходное кол-во камней в первой куче: '))
two = int(input('Исходное кол-во камней во второй куче: '))
while one >= 0 or two >= 0:
    if one == 0 and two == 0:
        break
    else:
        if one != 0 and two != 0 or one == 0 and two != 0 or one != 0 and two == 0:
            ii = random.randint(1, 10)
            if one == 0:
                a = 2
            elif two == 0:
                a = 1
            else:
                a = random.randint(1, 2)
            comp = one
            if a == 1:
                b = one
                one -= ii
                if one <= 0:
                    ii = b
                    one = 0
            elif a == 2:
                count2_pile = one
                two -= ii
                if two <= 0:
                    ii = count2_pile
                    two = 0
            if one <= 0 and two <= 0:
                print('Компьютер забрал', comp, 'камней. Осталось',
                      '0')
                print('Компьютер победил!')
                break
            else:
                print('Компьютер забрал', ii, 'камней из', a,
                      'кучи. Осталось', one, two)
                takes = int(input('Выберите кол-во камней: '))
                you = int(input('Выберите кучу: '))
                if you == 1:
                    one -= takes
                    print('Игрок забрал', takes, 'камней из', you,
                          'кучи. Осталось', one, two)
                elif you == 2:
                    two -= takes
                    print('Игрок забрал', takes, 'камней из', you,
                          'кучи. Осталось', one, two)
                if one <= 0 and two <= 0:
                    print('Игрок забрал', takes, 'камней. Осталось',
                          '0', '0')
                    print('Игрок победил!')
                    break
