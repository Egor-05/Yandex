a = input().split(',')
wrong = []
for i in a:
    s = 0
    for j in i:
        if ord('0') <= ord(j) <= ord('9'):
            s += 1
        elif ord(j) == ord('_'):
            s += 1
        elif ord('A') <= ord(j) <= ord('z'):
            s += 1
        elif ord('А') <= ord(j) <= ord('я'):
            s += 1
        else:
            break
    if s < len(i):
        wrong.append(i)
        wrong.sort()
a1 = 0
for e in wrong:
    if len(e) > a1:
        a1 = len(e)
for b in wrong:
    print(b.rjust(a1, ' '))
