tabl = []
a = int(input())
for i in range(a):
    cws = input().split("'")
    for j in range(len(cws)):
        if j % 2 == 0:
            cws[j] = cws[j].split(',')
            tabl.append(cws)
print(tabl)
nums = []
for i in range(int(input())):
    a = input().split()
    nums.append(a)
for i in nums:
    print(tabl[int(i[0])][int(i[1])])
