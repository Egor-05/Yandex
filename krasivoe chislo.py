a = int(input())
ma = max([int(i) for i in str(a)])
mi = min([int(e) for e in str(a)])
if ((ma + mi) / 2) == str(a - ma - mi):
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")