a = int(input())
for b in range(1, a + 1):
    for i in range(b - 1, -1, -1):
        print('Осталось секунд: ' + str(i))
    print('Пуск ' + str(b))
