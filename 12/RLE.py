a = input()
a = [int(i) for i in a]
k = 1
for j in range(len(a) - 1):
    if a[j] == a[j + 1]:
        k += 1
    else:
        b = a[j]
        print(k, a[j])
        k = 1
print(k, a[-1])
