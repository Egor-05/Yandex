b = input()
n = int(b[:4])
k = int(b[4:])
list_ = []
tt = 0
for i in range(n):
    m = input()
    p = int(m[:7])
    a = int(m[8:12])
    c = int(m[13:])
    if p * a != c:
        list_.append(str(i + 1))
        tt += p * a
    else:
        tt += c
print(k - tt)
print(' '.join(list_))
