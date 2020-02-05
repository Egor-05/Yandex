def hello(name):
    global n
    print(f'Здравствуйте, {name}! Вашу карту ищут...')
    n = name


def search_card(name):
    global base
    if name in base:
        print(f'Ваша карта с номером {base.index(name) + 1} найдена')
    else:
        print('Ваша карта не найдена')
