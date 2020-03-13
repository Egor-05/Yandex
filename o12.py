from datetime import datetime, timedelta


a = datetime(*[int(i) for i in input().split()])
number_of_days = int(input())
d_doze, g_doze = [float(i) for i in input().split()]
numod = 0
while d_doze > g_doze:
    d_doze /= 2
    numod += number_of_days
res = a + timedelta(days=numod)
print(res.year, res.month, res.day)
