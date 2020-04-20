nums = []
k = int(input())
for i in range(k):
    a = int(input())
    nums.append(a)
nums.sort(reverse=True)
for e in nums:
    print(e)
