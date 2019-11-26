n = int(input())
names = []
for i in range(n):
    name = input()
    names.append(name)
step = int(input())
rounds = int(input())
for j in range(rounds):
    del names[step - 1::step]
for e in names:
    print(e)
