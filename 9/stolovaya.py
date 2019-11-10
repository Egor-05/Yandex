befmeal = set()
meal = set()
km = int(input())
for i in range(km):
    allmeals = input()
    meal.add(allmeals)
days = int(input())
for j in range(days):
    nmd = int(input())
    for e in range(nmd):
        emd = input()
        befmeal.add(emd)
for b in (meal - befmeal):
    print(b)