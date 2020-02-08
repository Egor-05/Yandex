import sys
a = []
nums = []
s = 0
for i in sys.stdin:
    s += 1
    a.append(i.strip())
    if i.strip() != '':
        if i.strip()[0] == '#':
            nums.append(s)
a = list(filter(lambda x: True if len(x) > 0 and x[0] == '#' else False, a))
s = -1
for i in nums:
    s += 1
    print(f'Line {i}: {a[s][1:].strip()}')
