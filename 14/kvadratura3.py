a = input()
a = [int(i) for i in a.split()]
print(' '.join([str(i ** 2) for i in a]))
