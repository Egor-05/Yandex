list_ = []
for i in range(int(input())):
    a = input()
    if '/' in a:
        a = a.split(',')
        j = -1
        while j < len(a) - 1:
            j += 1
            s = -1
            while s < len(a[j]) - 1:
                s += 1
                if a[j][s] == '|':
                    a[j] = a[j] + ',' + a[j + 1]
                    del a[j + 1]
                if s >= len(a[j]):
                    break
    else:
        a = a.split(',')
    list_.append(a)
i = -1
while i < len(list_) - 1:
    i += 1
    if list_[i][-1][-2:] == 'nx':
        list_[i] += list_[i + 1]
        del list_[i + 1]
for _ in range(int(input())):
    s = [int(i) for i in input().split(',')]
    print(list_[s[0]][s[1]])
