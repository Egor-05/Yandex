a = int(input())
list_ = []
for i in range(a):
    prov = True
    a1 = input()
    a2 = a1.split()
    for j in a2:
        if 'лук' in j:
            prov = False
    if prov is True:
        list_.append(a1)
print(', '.join(list_))
