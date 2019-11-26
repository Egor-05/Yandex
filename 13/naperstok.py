n = int(input())
li = ['']*n
for i in range(n):
    li[i] = input()
k = int(input())
for i in range(k):
    x = int(input())
    tmp = ['']*x
    for j in range(x):
        tmp[j] = li[int(input())-1]
    li = tmp
for i in range(len(li)):
    print(li[i])