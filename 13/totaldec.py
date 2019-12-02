a = int(input())
sol = []
for i in range(a):
    a1 = input()
    sol.append(a1)
a2 = int(input())
rip = []
while len(sol) != 0:
    rip += sol[0::a2]
    del sol[::3]
print('\n'.join(rip))
