room = 1
while room > 0:
    if room == 1:
        print('Вы находитесь в пещере и видите три двери под номером 1, 2 и 3.')
        naprav = int(input())
        while naprav != 1 and naprav != 2 and naprav != 3:
            naprav = input()
        if naprav == 1:
            print('Вы пошли налево.')
            room = 2
        elif naprav == 2:
            print('Вы увидели дракона, который защщал своё сокровище.')
            room = -1
        elif naprav == 3:
            print('Вы зашли в тёмную комнату, через некоторое время вы упали к тоннелям')
            room = -1
    elif room == 2:
        print('Вы выберете «левый» или «правый»? Или повернёте «назад»?')
        naprav = input()
        while naprav != 'левый' and naprav != 'правый' and naprav != 'назад':
            naprav = input()
        if naprav == 'левый':
            print('Вы вернулись в тёмную комнату')
            room = -1
        elif naprav == 'правый':
            print('Вы смело вошли в правый тоннель. Но за ней вас поджидала ловушка,которая вас убила')
            room = -2
        elif naprav == 'назад':
            print('Вы отправились к начальной пещере.')
            room = 1