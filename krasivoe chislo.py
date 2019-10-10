a = input()
a1 = int(a) // 100
a2 = int(a) // 10 - a1 * 10
a3 = int(a) - a1 * 100 - a2 * 10
if a1 < a2:
    a1, a2 = a2, a1
if a1 < a3:
    a1, a3 = a3, a1
if a2 < a3:
    a2, a3 = a3, a2
if (a1 + a3) / 2 == a2:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")