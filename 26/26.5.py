from itertools import permutations
dictionary = input().lower().split()
letter = input().lower().split()
ln = []
for i in letter:
    b = True
    for j in permutations(i, len(i)):
        if ''.join(j) in dictionary and ''.join(j) != i:
            b = False
            break
    if b:
        ln.append(i)
    else:
        ln.append('#' * len(i))
print(' '.join(ln))
