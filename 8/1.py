a = int(input())
for n in range(1, a + 1):
    print(n, end='	')
    for i in range(2, a + 1):
        print(n * i, end='	')
    print()