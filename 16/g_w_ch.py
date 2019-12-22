a = int(input())
hod = False
if input() == 'Маша':
    hod = True
else:
    hod = False
nums = []
for i in range(int(input())):
    if hod is True:
        a = a * 3 - 2
        nums.append(a)
    else:
        while a % 2 == 0 or a % 3 == 0:
            if a % 2 == 0:
                a /= 2
            elif a % 3 == 0:
                a /= 3
            nums.append(a)
        a += 11
        nums.append(a)
    hod = not hod
nums.sort()
#  if len(nums) > 2:
#      while len(nums) != 1 or len(nums) != 2:
#          del nums[0]
#          del nums[-1]
print(nums)
