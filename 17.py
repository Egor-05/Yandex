pros = {}
a = int(input())
a1 = input().split(' опубликовал пост, количество просмотров: ')
a1[-1] = int(a1[-1])
pros[a1[0]] = a1[-1]
for i in range(a - 1):
    a2 = input().split(' отрепостил пост у ')
    a2[-1] = a2[-1].split(', количество просмотров: ')
    a2 += a2[-1]
    del a2[1]
    pros[a2[0]] = int(a2[-1])
    if a2[1] in pros and a2[1] != a1[0]:
        pros[a2[1]] += int(a2[-1])
    pros[a1[0]] += int(a2[-1])
for i in pros:
    print(pros[i])
