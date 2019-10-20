a = input()
b = 190
s = 0
n = 0
while a != "!":
    if 150 <= int(a) <= 190:
        n += 1
        if int(b) > int(a):
            b = a
        if int(s) < int(a):
            s = a
    a = input()
print(n)
print(b, s)
