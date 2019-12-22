al = []
for i in range(int(input())):
    pir = []
    a = input().split()
    a = [int(j) for j in a]
    for _ in range(len(a)):
        if a[0] >= a[-1]:
            pir.append(a[0])
            del a[0]
        else:
            pir.append(a[-1])
            del a[-1]
    al.append(pir)
for i in al:
    a = False
    if len(i) > 1:
        for j in range(len(i) - 1):
            if i[j] < i[j + 1]:
                a = True
                break
        if a is False:
            i = [str(b) for b in i]
            print(' '.join(i))
        else:
            print('НЕТ')
    else:
        print(i[0])
