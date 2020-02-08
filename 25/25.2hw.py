import sys
from collections import defaultdict
words = []
for i in sys.stdin:
    if '\n' not in i:
        words.append(i)
    else:
        words.append(i[:-1])
d_o_w = defaultdict(list)
for i in words:
    code_i = 0
    for j in i.upper():
        if j != '\n':
            code_i += (ord(j) - ord('A') + 1)
    d_o_w[code_i].append(i)
s = []
for i in sorted(d_o_w):
    for j in sorted(d_o_w[i]):
        s.append(j)
for i in s:
    print(i)