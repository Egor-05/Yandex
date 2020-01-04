a = int(input())
list_ = [input() for _ in range(a)]
i = 0
while i < len(list_):
    i += 1
    j = 0
    while j < len(list_[i]):
        j += i
        list_[i][j] += ','
a = int(input())
for _ in range(a):
    s = [int(i) for i in input().split(',')]
    print(list_[s[0]][s[1]])
