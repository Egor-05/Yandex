n = int(input())
Evrasia = False
Ostasia = True
for i in range(n):
    a = input()
    if a == 'Меняем':
        Evrasia = not Evrasia
        Ostasia = not Ostasia
    elif a == 'С кем война?':
        if not Evrasia:
            print('Евразия')
        if not Ostasia:
            print('Остазия')
    else:
        if Evrasia:
            print('Евразия')
        if Ostasia:
            print('Остазия')
