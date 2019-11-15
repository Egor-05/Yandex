a = int(input())
for i in range(a):
    ad = input()
    if ad[:3] == 'Не ':
        print(ad[3:])
    else:
        print(ad)
