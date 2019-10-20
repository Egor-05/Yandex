a = 0
b = 0
for i in range(int(input())):
    i = int(input())
    if a == 0:
        b += i
        a += i
    else:
        b -= i
        a = 0
print(b)
