pros = {}
a = int(input())
a1 = input().split(' опубликовал пост, количество просмотров: ')
a1[-1] = int(a1[-1])
pros[a1[0]] = {'from': '', 'count': a1[-1]}
for i in range(a - 1):
    a2 = input().split(' отрепостил пост у ')
    a2[-1] = a2[-1].split(', количество просмотров: ')
    a2 += a2[-1]
    del a2[1]
    pros[a2[0]] = {'from': a2[1], 'count': int(a2[-1])}
# dict0 = {'b': 100, 'c': 200, 'd': 300}
lk = [i for i in pros]
lk.reverse()
for i in lk:
    if pros[i]['from'] in pros:
        pros[pros[i]['from']]['count'] += pros[i]['count']
lk.reverse()
for i in lk:
    print(pros[i]['count'])
