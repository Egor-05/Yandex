elem = []
a = int(input())
for i in range(a):
    a1 = input()
    elem.append(a1)
pos = int(input())
for i in elem:
    if pos <= len(i):
        print(i[pos - 1], end='')