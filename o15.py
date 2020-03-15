a = input()
max_len = (len(a) - 3) // 2
s = 'NO'
for i in range(1, max_len + 1):
    if (len(a) - 2 * i) % 3 == 0:
        interv = (len(a) - 2 * i) // 3
        s1 = a[:interv]
        s2 = a[interv:interv + i]
        s3 = a[interv + i:2 * interv + i]
        s4 = a[2 * interv + i: 2 * interv + 2 * i]
        s5 = a[2 * interv + 2 * i:]
        if s1 == s3 == s5 and s2 == s4:
            s = s2
            break
print(s)