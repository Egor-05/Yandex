a = int(input())
for i in range(a):
    ad = input()
    if ad[:3] == (chr(1053) or chr(1085)) + chr(1077) + chr(32):
        print(ad[3:])
    else:
        print(ad)
