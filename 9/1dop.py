fridge = set()
k = int(input())
for i in range(k):
    pfridge = input()
    fridge.add(pfridge)
rk = int(input())
for j in range(rk):
    p = input()
    pk = int(input())
    neededproducts = set()
    for b in range(pk):
        np = input()
        neededproducts.add(np)
    if neededproducts.issubset(fridge) or neededproducts in fridge:
        print(p)
