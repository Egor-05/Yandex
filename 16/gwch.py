a = int(input())
hod = False
if input() == 'Маша':
    hod = True
nums = []
for i in range(int(input())):
    if hod is True:
        a = a * 3 - 2
        nums.append(a)
    else:
        while a % 2 == 0:
            a /= 2
        while a % 3 == 0:
            a /= 3
        a += 11
        nums.append(a)
    hod = not hod
nums.sort()
if len(nums) % 2 == 0:
    print((nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2)
else:
    print(nums[len(nums) // 2])
