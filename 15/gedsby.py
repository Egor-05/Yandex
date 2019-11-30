a = input()
b = input()
b = b.split()
for i in b:
    c = i.lower()
    if a in c:
        print(i)
