def ask_password():
    n = False
    for i in range(3):
        s = input()
        if s == 'password':
            print("Пароль принят")
            n = True
    if n is False:
        print("В доступе отказано")
