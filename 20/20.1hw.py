rus = ['январь',
       'февраль',
       'март',
       'апрель',
       'май',
       'июнь',
       'июль',
       'август',
       'сентябрь',
       'октябрь',
       'ноябрь',
       'декабрь']

eng = ['january',
       'february',
       'march',
       'april',
       'may',
       'june',
       'july',
       'august',
       'september',
       'october',
       'november',
       'december']


def month_name(num, leng):
    if leng == "en":
        return eng[num - 1]
    else:
        return rus[num - 1]