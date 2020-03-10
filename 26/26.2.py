import sys
from functools import reduce
words = []
for i in sys.stdin:
    if '\n' in i:
        i = i[:-1]
    words.append(i)
res = reduce(lambda x, y: x if x < y else y, words)
print(words)