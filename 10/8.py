a = input()
while a[0] != 1 or int(a) < 1000000000:
    a = int(a) * int(a[0])
    a = str(a)
    if int(a[0]) == 1 or int(a) >= 1000000000:
        break
print(a)
