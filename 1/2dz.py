import datetime


def f(n):
    return f(n - 1) * n if n else 1


znach = int(input())
a = datetime.datetime.now()
b = f(znach)
print(b)
print(datetime.datetime.now() - a)
s = 1
x = datetime.datetime.now()
for i in range(1, znach + 1):
    s *= i
print(s)
print(datetime.datetime.now() - x)
