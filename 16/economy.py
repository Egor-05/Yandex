a = int(input())
list_ = [['0']]
for i in range(a - 1):
    a1 = input().split()
    a1.append('0')
    list_.append(a1)
tabl = []
for i in range(a):
    row = ''
    for j in range(a):
        if i == j:
            row += '0 '
        elif j < i:
            row += list_[i][j] + ' '
        else:
            row += list_[j][i] + ' '
    tabl.append([int(e) for e in row.split()])
pay = []
for i in range(a):
    for j in range(a):
        for b in range(a):
            if tabl[i][b] > tabl[i][j] + tabl[j][b]:
                if [b, i] not in pay and [i, b] not in pay:
                    pay.append([i, b])
pay.sort()
for i in range(1, len(pay)):
    if pay[i] == pay[i - 1]:
        del pay[i]
for i in pay:
    i = [str(j) for j in i]
    print(' '.join(i))
