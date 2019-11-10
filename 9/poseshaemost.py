e = set()
for i in range(int(input())):
    d = set()
    for j in range(int(input())):
        d.add(input())
    if i > 0:
        e = d & e
    else:
        e = d
for name in e:
    print(name)
