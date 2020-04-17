a = [int(i) for i in input().split()]
for i in range(int(input())):
    s = input()
    if s == 'make_negative':
        a = [j * (-1 * (j // abs(j) if j != 0 else 1)) for j in a]
    elif s == 'square':
        a = [j ** 2 for j in a]
    elif s == 'strange_command':
        a = [j + (not j % 5) for j in a]
print(' '.join([str(i) for i in a]))
