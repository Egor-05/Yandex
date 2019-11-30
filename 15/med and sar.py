a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
print(sum(a) / len(a))
a = a.sort
while a != 1 or a != 2:
    del a[0]
    del a[-1]
print(sum(a) / len(a))
