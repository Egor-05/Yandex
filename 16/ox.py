def prov(s):
    if 'ooo' in s:
        print('o')
        return True
    elif 'xxx' in s:
        print('x')
        return True

b = False
matrix = []
a = int(input())
for _ in range(a):
    a1 = [j for j in input()]
    matrix.append(a1)
for i in range(a):
    s = ''.join([matrix[i][j] for j in range(a)])
    b = prov(s)
    if b:
        break
for i in range(a):
    s = ''.join([matrix[j][i] for j in range(a)])
    b = prov(s)
    if b:
        break
if b is False:
    print('-')
