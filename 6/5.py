a = 1
for i in range(6):
    a1 = int(input())
    if a1 == 0:
        a1 += 1
    a *= a1
print(a)