chisla = []
a = int(input())
for i in range(a):
    a1 = int(input())
    chisla.append(a1)
for i in range(len(chisla) - 1):
    print(chisla[i] + chisla[i + 1])