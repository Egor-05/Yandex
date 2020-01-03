a = int(input())
list_ = [input() for _ in range(a)]
a = int(input())
for _ in range(a):
    s = [int(i) for i in input().split(',')]
for i in range(len(list_)):
    j = -1
    while j < len(list_[i]):
        j += 1
        if "'" in list_[i][j]:
            list_[i][j] = list_[i][j].split()
