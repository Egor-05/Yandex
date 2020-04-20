cities = set()
s = int(input())
for i in range(s):
    d = input()
    cities.add(d)
b = input()
if b in cities:
    print('TRY ANOTHER')
else:
    print('OK')