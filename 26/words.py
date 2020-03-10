import sys
li = []
count = 0
for i in sys.stdin:
    if '\n' in i:
        i = i[:-1]
    if i not in li:
        li.append(i)
    else:
        count += int(i.split()[0])
print(count)
