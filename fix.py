from swift import words
from collections import defaultdict
from random import choice

wrds = defaultdict(list)
for i in range(len(words) - 1):
    wrds[words[i]].append(words[i + 1])

a = input().lower()
print(a.capitalize(), end=' ')
if a not in wrds:
    print(f'Слова {a} нет в тексте.')
else:
    j = 0
    while j < 3:
        a = choice(wrds[a])
        print(a, end=' ')
        if a == '.':
            j += 1
