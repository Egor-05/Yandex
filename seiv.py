a = input()
a1 = int(a) // 100
a2 = int(a) // 10 - a1 * 10
a3 = int(a) - a1 * 100 - a2 * 10
b = input()
b1 = int(a) // 100
b2 = int(a) // 10 - a1 * 10
b3 = int(a) - a1 * 100 - a2 * 10
if a1 == b1 and a2 == b2 and a3 == b3:
    print("ОК")
if (a1 == b1 and a2 == b2) or (a2 == b2 and a3 == b3) or (a1 == b1 and b3 == a3):
    print("В числе две одинаковые цифры")
if ((a1 == b1 or a1 == b2 or a1 == b3) and (a2 == b1 or a2 == b2 or a2 == b3) and
        (a3 == b1 or a3 == b2 or a3 == b3)):
    print("В числе все цифры одинаковые")