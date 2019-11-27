a = input().split()
print(' '.join([str(int(i) ** 2) for i in a if int(i) % 2 == 1 and str(int(i) ** 2)[-1] != '9']))
