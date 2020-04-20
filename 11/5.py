a = int(input())
for _ in range(a):
    s = 0
    ad = input()
    for i in ad[:3]:
        if ord(i) == ord('Н') or ord(i) == ord('н'):
            s += 1
        elif ord(i) == ord('е'):
            s += 1
        elif ord(i) == ord(' '):
            s += 1
    if s == 3:
        print(ad[3:])
    else:
        print(ad)
