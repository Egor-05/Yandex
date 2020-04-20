text = input()
text1 = input()
if "@" not in text and "@" in text1:
    print("OK")
elif "@" in text and "@" in text1:
    print("Некорректный логин")
elif "@" not in text and "@" not in text1:
    print("Некорректный адрес")
else:
    print("Некорректный логин")

