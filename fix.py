a = input()
c = a[(len(a) - 1) // 2 + 1]
pal = (a[:(len(a) - 1) // 2 + 1] + c + a[:(len(a) - 1) // 2 + 1][::-1] if len(a) % 2 == 1 else a[:2] + a[:2][::-1])
print(pal)
if int(pal) < int(a):
    if len(pal) % 2 == 0:
        a = pal[len(pal) // 2]
        a1 = pal[len(pal) // 2 + 1]
        pal = pal[:len(pal) // 2] + a + a1
else:
    print(pal)