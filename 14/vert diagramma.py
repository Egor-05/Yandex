a = [int(i) for i in input().split()]
print('*' * (len(a) + 2))
print('*' + ' ' * len(a) + '*')
for i in range(max(a), 0, -1):
    print('*', end='')
    for j in a:
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print('*')
