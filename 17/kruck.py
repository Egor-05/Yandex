li = []
s = 0
for i in range(int(input())):
    a = input().split()
    if i == 0:
        li = a
    else:
        if a[0][0] == li[0][0]:
            s += 1
            li = a
print(s)