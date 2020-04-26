from sys import stdin
from collections import defaultdict


offers = defaultdict(set)
for i in stdin:
    i = i.strip('\n').split(' - ')
    offers[i[0]].add(i[1])
for i in offers:
    print(f'{i}: {"; ".join([i for i in offers[i]])}')
