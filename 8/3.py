k = int(input())
schet = 0
s = 0
for i in range(1, k + 1):
    print(i, end=' ')
    s += 1
    if s > schet:
        print()
        schet = s
        s = 0
