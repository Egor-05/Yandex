def squared():
    s = 0
    for i in range(11, 100):
        if i % 10 == 0:
            continue
        s += 1
        if s % 9 != 0:
            print(str(i ** 2).ljust(4, ' '), end=' ')
        else:
            print(str(i ** 2), end='\n')
