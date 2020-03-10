import sys
import math
from functools import reduce
nums = [i[:-1] for i in sys.stdin]
while len(nums) > 0:
    nums = list(reduce(lambda x, y: [x, y], nums))
    snams = []
    for i in nums:
        print(i[0], i[1])
        snams.append(str(math.gcd(int(i[0]), int(i[1]))))
    nums = snams
print(*nums)
