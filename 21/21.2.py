from itertools import product


mast = ['пик', 'треф', 'бубен', 'червей']
nom = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
res = set()
for i in list(product(nom, mast, nom, mast, nom, mast)):
    if 'червей' in i and ('валет' in i or 'дама' in i or 'король' in i or 'туз' in i):
        a = [f'{i[0]} {i[1]}', f'{i[2]} {i[3]}', f'{i[4]} {i[5]}']
        if len(a) == len(set(a)):
            res.add(', '.join(sorted(a)))

res = list(res)
res.sort()
for i in res:
    print(i)
