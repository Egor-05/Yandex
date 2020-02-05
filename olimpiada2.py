a = int(input())
a1 = input().split()
a1 = [int(i) for i in a1]
code = ''
for i in range(a):
    s = ''
    word = input()
    word1 = set(word)
    for j in word1:
        if word.count(j) == a1[i]:
            s += j
    if len(s) != 1:
        break
    else:
        code += s
pr = ''
if len(code) != a:
    print('NO')
else:
    print(code)
