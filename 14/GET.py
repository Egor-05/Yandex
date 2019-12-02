a = input()
b = input()
a = a.split('?')
a1 = a[1].split('&')
for i in a1:
    if b in i:
        a2 = i.split('=')
print(a2[1])
