houses1 = set()
houses2 = set()
while 1:
    a = input()
    houses1.add(a)
    if a == '':
        break
while 1:
    b = input()
    houses2.add(b)
    if b == '':
        break
if (len(houses1 & houses2) - 1) != 0:
    for i in houses1 & houses2:
        print(i)
else:
    print('EMPTY')