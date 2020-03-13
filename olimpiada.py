valuable_items = []
impurities = []
for _ in range(int(input())):
    a = input().split()
    valuable_items.append([int(i) for i in a[:-1]])
    impurities.append(1 - int(a[-1]) / 100)
needed_item = int(input()) - 1
result = [i[needed_item] * j for i, j in zip(valuable_items, impurities) if len(i) > needed_item]
if int(sum(result)) == sum(result):
    print(int(sum(result)))
else:
    print(sum(result))
