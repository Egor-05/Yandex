import math
from functools import reduce
from sys import stdin


lst = list(map(int, [i for i in stdin]))
print(reduce(math.gcd, lst))
