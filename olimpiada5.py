a = int(input())
mushrooms = [int(i) for i in input().split()]
mushrooms.sort(reverse=True)
if mushrooms[-1] == 0:
    del mushrooms[-1]
mm = min(mushrooms)
d_f_r = [i for i in range(mm, 0, -1) if mm % i == 0]
for i in d_f_r:
    found = True
    for j in mushrooms:
        if j % i != 0:
            found = False
            break
    if found:
        break
print(i)
