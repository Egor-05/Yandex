y = int(input())
y = 1 / y
y = [y]
y1 = [int(j) for j in y]
a1 = set()
a2 = [i for i in y1 if y1[i] > 1]
print(''.join(str(a2)))
