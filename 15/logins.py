a = input().split(',')
wrong = [i for i in a if not i.replace('_', '').isalnum()]
a1 = 0
for e in wrong:
    if len(e) > a1:
        a1 = len(e)
wrong.sort()
for b in wrong:
    print(b.rjust(a1, ' '))
