class Transport:
    def __init__(self, number, speed, oil=0):
        self.num = number
        self.oil = oil
        self.speed = speed

    def return_distance(self, time, length):
        d1 = self.speed * time % length
        d2 = length - d1
        return d1 if d1 < d2 else d2


class Car(Transport):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed *= (1 - (98 - self.oil) / 30)


class Motorcycle(Transport):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed *= (1 - (98 - self.oil) / 30 * 2)


n, m, t = [int(i) for i in input().split()]
tr = []
for i in range(n):
    a = [int(i) for i in input().split()]
    if a[1] == 1:
        tr.append(Car(a[0], a[2], a[3]))
    elif a[1] == 2:
        tr.append(Motorcycle(a[0], a[2], a[3]))
    else:
        tr.append(Transport(a[0], a[2]))
tr1 = sorted([(i.num, i.return_distance(t, m)) for i in tr], key=lambda x: x[1])
print(min([i[0] for i in filter(lambda x: x[1] == tr1[0][1], tr1)]))
