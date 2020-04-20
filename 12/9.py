ch = []
sum = 0
a = int(input())
for i in range(a):
    a1 = int(input())
    ch.append(a1)
beg = int(input())
end = int(input())
ch = ch[beg - 1:end]
for e in ch:
    sum += e
print(sum)