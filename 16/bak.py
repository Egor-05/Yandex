a = int(input())
field = []
for _ in range(a):
    list_ = []
    for _ in range(a):
        list_.append(int(input()))
    field.append(list_)
for i in range(int(input())):
    x = int(input())
    y = int(input())
    field[y][x] -= 4
    if field[y][x] < 0:
        field[y][x] = 0
    for j in range(y - 1, y + 2):
        for e in range(x - 1, x + 2):
            if (a > e >= 0) and (0 <= j < a):
                field[j][e] -= 4
                if field[j][e] < 0:
                    field[j][e] = 0
for i in field:
    for j in i:
        i = [str(j) for j in i]
    print(' '.join(i))
