listA = [' * ',
         '* *',
         '***',
         '* *',
         '* *']
listB = ['** ',
         '* *',
         '** ',
         '* *',
         '** ']
listC = [' * ',
         '* *',
         '*  ',
         '* *',
         ' * ']
a = input()
for i in range(5):
    for j in a:
        if j == 'A':
            print(listA[i], end='  ')
        elif j == 'B':
            print(listB[i], end='  ')
        else:
            print(listC[i], end='  ')
    print()
