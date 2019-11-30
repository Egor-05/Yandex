a = input()
a = a.lower()
b = set()
c = []
g = 0
for i in a:
    b.add(i)
    c.append(i)
e = list(b)
for j in range(len(e)):
    if c.count(e[j]) > g:
        g = c.count(e[j])
print(g)