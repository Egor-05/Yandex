a = [int(i) for i in input().split()]
names = [input() for i in range(a[0])]
win = []
for i in range(a[1]):
    num = 0
    a1 = input()
    s = 1
    for j in range(len(a1)):
        if a1[j].isdigit() and s == 1:
            num += int(a1[j])
            s += 1
        elif a1[j].isdigit() and a1[j - 1].isdigit():
            num += int(a1[j])
    win.append(''.join([a1[j] for j in range(num - 1, len(a1), num)]))
pr = []
for i in win:
    for j in names:
        if i.lower() == j.lower():
            if j not in pr:
                pr.append(j)
            break
if len(pr) > 0:
    print('\n'.join(pr))
else:
    print('NO')
