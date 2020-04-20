a = input()
b = input()
c = len(a)
if c < 8:
    print("Короткий!")
elif b != a:
    print("Различаются.")
elif "123" in a:
    print("Простой!")
else:
    print("OK")