cnt = int(input())
every = []
elite = []
for i in range(cnt):
    n = input()
    nspl = n.split()
    if nspl[1] in ('4', '5'):
        elite.append(n)
    every.append(n)
for e in every:
    print(e)
print()
for j in elite:
    print(j)
