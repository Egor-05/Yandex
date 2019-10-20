door1level = 0
while door1level != 1 and door1level != 2 and door1level != 3 and door1level == 'назад' and door1level != 0:
    door1level = int(input())
while str(door1level) != 'стоп':
    if door1level == 0:
        print("Вы очнулись в тёмной пещере, когда вы огляделись то увидели три выхода под номером 1, 2 и 3.")
        print("Укажите число выбранной вами двери!")
    if door1level == 1:
        print("Когда вы зашли в первую дверь вы чуть не провалились в глубокую яму, "
          "но к счастью всё обошлось и вы увидели ещё две двери")
        print("Укажите номер следующей двери в которую вы зайдете.")
        if str(door1level) == 'назад':
            door1level = 0
        door1_2level = int(input())
        while door1_2level != 1 and door1_2level != 2 and door1_2level == 'назад':
            door1_2level = int(input())
        if door1_2level == 1:
            print("Как только вы вошли в дверь на вас напала гигантская оса и "
                  "после долгой битвы смогла таки вас одолеть.")
            if str(door1_2level) == 'назад':
                door1level = 0
        else:
            print("Вы вошли в высокую пещеру с отверстием в потолке и через большое количество попыток "
                  "смогли выбраться. УРА ПОБЕДА!!!")
            if str(door1_2level) == 'назад':
                door1level = 0
    elif door1level == 2:
        print("Открыв дверь вы неосторожно вожли в пещеру наступив на хвост дракону,"
              " который проснувшись сжёг вас до тла.")
        if str(door1level) == 'назад':
            door1level = 0
    elif door1level == 3:
        print("Вы очень проголодались и увидев грибы съели очень много и"
              " скончались от сильных болей в животе.")
        if str(door1level) == 'назад':
            door1level = 0
