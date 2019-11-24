a = int(input())
prov = False
nums = []
for i in range(a):
    num = int(input())
    nums.append(num)
n = int(input())
for j in range(1, len(nums)):
    if nums[j - 1] * nums[j] == n:
        prov = True
if prov:
    print('Да')
else:
    print('Нет')
