def late(now, classes, bus):
    nt = [int(i) for i in now.split(':')]
    ct = [int(i) for i in classes.split(':')]
    t = (ct[0] - nt[0]) * 60 + (ct[1] - nt[1])
    c = 0
    if max(bus) < 5 or t < 0:
        return 'Опоздание'
    a = ''
    while c < len(bus):
        if bus[c] < 5:
            c += 1
            continue
        if bus[c] + 15 > t and a == '':
            return 'Опоздание'
        elif bus[c] + 15 > t and a != 0:
            break
        a = bus[c] - 5
        c += 1
    return f'Выйти через {a} минут'
