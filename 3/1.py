i = input()
a = input()
if i == "Тула" and not a == "Пенза" and not a == "Тула":
    print("ДА")
elif not i == "Тула" and a == "Пенза" and not i == "Пенза":
    print("ДА")
else:
    print("НЕТ")