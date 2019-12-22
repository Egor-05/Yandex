a = int(input())
list_ = [['0']]
for i in range(a - 1):
    a1 = input().split()
    a1.append('0')
    list_.append(a1)
for i in range(a):
    row = ''
    for j in range(a):
        if i == j:
            row += '0 '
        elif j < i:
            row += list_[i][j] + ' '
        else:
            row += list_[j][i] + ' '
    print(row)
