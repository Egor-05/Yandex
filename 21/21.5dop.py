dict_ = {}


def get_transactions(t):
    global dict_
    if t != 'print_it':
        cost = int(t.split(':')[-1])
        func = t.split('-')[-1].split(':')[0]
        if func not in dict_:
            dict_[func] = [1, cost]
        else:
            dict_[func][0] += 1
            dict_[func][1] += cost
    else:
        for i in dict_:
            print(f'{dict_[i][0]} {i} {dict_[i][1]}')
