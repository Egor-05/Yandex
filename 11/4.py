a = int(input())
for i in range(a, 0, -1):
    for j in range(0, a):
        b = chr(ord('A') + j)
        print(b + str(i), end=' ')
    print()