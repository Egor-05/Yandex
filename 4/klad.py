a = 0
x = int(input())
y = int(input())
x1 = 0
y1 = 0
n = 0  # направление, 0 - север, 1 - восток, 2 - юг, 3 - запад
b = input()
if x == 0 and y == 0:
    print(0)
while (x == x1) and (y == y1):
    if b == 'вперёд':
        steps = int(input())
    a += 1
    n %= 4
    if b == 'вперёд' and n == 0:
        y1 += steps
    elif b == 'вперёд' and n == 1:
        x1 += steps
    elif b == 'вперёд' and n == 2:
        y1 -= steps
    elif b == 'вперёд' and n == 3:
        x1 -= steps
    if b == 'направо':
        n += 1
    elif b == 'разворот':
        n += 2
    elif b == 'налево':
        n += 3
    b = input()
print(a)
if n == 0:
    print('север')
elif n == 1:
    print('восток')
elif n == 2:
    print('юг')
elif n == 3:
    print('запад')
