length = int(input())
width = int(input())
list1 = []
for i in range(length):
    a = input()
    list1.append(a)
list2 = []
for j in list1[::2]:
    list2.append(j[::2])
    length = length // 2 + 1
    width = width // 2
for e in list2:
    print(e)
