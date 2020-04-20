zaprosy = []
a = int(input())
for i in range(a):
    a1 = input()
    zaprosy.append(a1)
poisk = input()
for i in zaprosy:
    if poisk in i:
        print(i)