def late(now, classes, bus):
    nt = [int(i) for i in now.split(':')]
    ct = [int(i) for i in classes.split(':')]
    t = (ct[0] - nt[0]) * 60 + (ct[1] - nt[1]) - 15
    c = 0
    if max(bus) < 5 or t < 0:
        return 'Опоздание'
    while c < len(bus):
        if bus[c] < 5:
            c += 1
            continue
        if t + 5 - bus[c] < 0 and bus[c - 1] - 5 < 0:
            return 'Опоздание'
        elif t + 5 - bus[c] < 0 and bus[c - 1] - 5 >= 0:
            break
        c += 1
    return f'Выйти через {bus[c - 1] - 5} минут'


print(late('12:59', '13:45', [3, 35, 46, 55]))
print(late('9:20', '9:35', [4, 25, 30]))
print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('13:50', '14:30', [7, 17, 35, 48]))