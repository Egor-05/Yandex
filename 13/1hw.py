a = int(input())
n = [''] * a
for i in range(a):
    n[i] = input()
k = int(input())
for i in range(k):
    b = int(input())
    t = [''] * b
    for j in range(b):
        t[j] = n[int(input()) - 1]
    n = t
for i in range(len(n)):
    print(n[i])
