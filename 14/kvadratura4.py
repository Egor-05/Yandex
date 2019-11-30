a = [int(i) for i in input().split()]
print(' '.join([str(i ** 2) for i in a if i % 2 == 1 and str(i ** 2)[-1] != '9']))
