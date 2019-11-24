num = []
name = []
a = int(input())
for i in range(a):
    nam = input()
    name.append(nam)
    kol = input()
    num.append(kol)
for j in range(a - 1, -1, -1):
    print(name[j], num[j])
