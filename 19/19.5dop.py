def tic_tac_toe(field):
    d1 = field[0][0] + field[1][1] + field[2][2]
    d2 = field[0][2] + field[1][1] + field[2][0]
    if d1.count('0') == 3:
        print('0 win')
        return
    elif d2.count('0') == 3:
        print('0 win')
        return
    if d1.count('x') == 3:
        print('x win')
        return
    elif d2.count('x') == 3:
        print('x win')
        return

    for i in range(3):
        v = field[0][i] + field[1][i] + field[2][i]
        if v.count('0') == 3:
            print('0 win')
            return
        elif v.count('x') == 3:
            print('x win')
            return
    for i in field:
        if ''.join(i).count('0') == 3:
            print('0 win')
            return
        elif ''.join(i).count('x') == 3:
            print('x win')
            return
    print('draw')
