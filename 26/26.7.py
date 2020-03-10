import sys
import math
nums = [int(i) for i in sys.stdin]
while len(nums) > 1:
    n = set()
    numrev = nums[::-1]
    for i in zip(nums, numrev):
        n.add(math.gcd(i[0], i[1]))
    nums = list(n.copy())
print(*nums)
