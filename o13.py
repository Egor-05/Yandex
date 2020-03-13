from datetime import datetime


d1 = datetime(*[int(i) for i in input().split()])
d2 = datetime(*[int(i) for i in input().split()])
delta = d2 - d1
birthday = datetime(*[int(i) for i in input().split()])
day_of_death = datetime(*[int(i) for i in input().split()])
a = ((datetime.toordinal(birthday) - datetime.toordinal(d1) % delta.days) // delta.days + 1)\
    * delta.days + datetime.toordinal(d1) % delta.days
a = datetime.fromordinal(a)
print(max((day_of_death - a).days // delta.days + 1, 0))
