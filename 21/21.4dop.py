horses = []


def do_bet(f, s):
    if f not in horses and s != 0 and 0 < f < 11:
        print(f'Ваша ставка в размере {s} на лошадь {f} принята')
        horses.append(f)
    else:
        print('Что-то пошло не так, попробуйте еще раз')
