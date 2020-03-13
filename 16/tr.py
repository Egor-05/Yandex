a = int(input())
tr = [['1'], ['1', '1']]
for i in range(a - 2):
    a1 = []
    a1.append('1')
    for j in range(len(tr[-1]) - 1):
        a1.append(str(int(tr[-1][j]) + int(tr[-1][j + 1])))
    a1.append('1')
    tr.append(a1)
for i in range(a):
    print(' '.join(tr[i]))
