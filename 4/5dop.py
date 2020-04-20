a = input()
b = input()
c = len(a)
while a != b or c < 8 or "123" in a:
    if c < 8:
        print("Короткий!")
        a = input()
        b = input()
        c = len(a)
    elif "123" in a:
        print("Простой!")
        a = input()
        b = input()
        c = len(a)
    elif b != a:
        print("Различаются.")
        a = input()
        b = input()
        c = len(a)
    else:
        print("OK")
print("OK")