a = int(input)
if a < 0:
    print('Пуск')
else:
    for i in range(a, -1, -1):
        print('Осталось секунд:', i)
    print('Пуск')
