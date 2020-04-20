a = int(input())
s = 0
mini = 0
for i in range(1, a + 1):
    mi = 999
    n = int(input())
    for h in range(n):
        c = int(input())
        if c < mi:
            mi = c
    if mi > mini:
        mini, mi = mi, 999
        s = i
print(s, mini)
