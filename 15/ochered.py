a = int(input())
list_ = []
for i in range(a):
    a1 = input()
    s = 0
    if ' встал в очередь' in a1:
        a1 = a1[:a1.find(' встал в очередь.')]
        list_.append(a1)
    elif ' встала в очередь.' in a1:
        a1 = a1[:a1.find(' встала в очередь.')]
        list_.append(a1)
    elif ' будет за тобой.' in a1:
        a1 = a1[:a1.find(' будет за тобой.')]
        a1 = a1.replace('Привет, ', '')
        a1 = a1.split('! ')
        list_.insert((list_.index(a1[0]) + 1), a1[1])
    else:
        a1 = a1[:a1.find(', хватит тут стоять, пошли отсюда.')]
        if a1 in list_:
            del list_[list_.index(a1)]
print('\n'.join(list_))
