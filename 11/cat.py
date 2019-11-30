n = int(input())
for i in range(n):
    s = input()
    pos = s.find('кот')
    if pos != -1:
        print(i + 1, pos + 1)
