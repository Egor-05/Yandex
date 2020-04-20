a = input()
a1 = int(a) // 100
a2 = int(a) // 10 - a1 * 10
a3 = int(a) - a1 * 100 - a2 * 10
if a1 != a2 and a2 != a3 and a1 != a3:
    print("ОК")
elif a1 == a2 and a2 == a3 and a1 == a3:
    print("В числе все цифры одинаковые")
elif (a1 == a3) or (a2 == a3) or (a1 == a2):
    print("В числе две одинаковые цифры")
else:
    print("")
