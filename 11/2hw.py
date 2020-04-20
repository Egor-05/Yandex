a = int(input())
for i in range(a):
    s = input()
    if s[:2] == '%%':
        print(s[2:])
    elif s[:4] == '####':
        b = 0
    else:
        print(s)
