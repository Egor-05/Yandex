a = int(input())
nums = []
for i in range(a):
    num = int(input())
    nums.append(num)
n = int(input())
prov = False
for j in range(len(nums)):
    for e in range(len(nums)):
        if e == j:
            if e < (len(nums) - 1):
                e += 1
            else:
                e -= 1
        if nums[e] * nums[j] == n:
            prov = True
if prov:
    print('ДА')
else:
    print('НЕТ')
