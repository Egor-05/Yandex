a = input()
a = a.replace(' ', '')
a = a.lower()
b = set(i for i in a)
g = 0
for j in b:
    if a.count(j) > g:
        d, g = j, a.count(j)
    elif a.count(j) == g:
        if ord(j) < ord(d):
            d, g = j, a.count(j)
print(d)
