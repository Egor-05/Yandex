name_and_date = []


def setup_profile(name, vacation_dates):
    global name_and_date
    name_and_date = [name, vacation_dates]


def print_application_for_leave():
    global name_and_date
    print(f'Заявление на отпуск в период {name_and_date[1]}. {name_and_date[0]}')


def print_holiday_money_claim(amount):
    global name_and_date
    print(f'Прошу выплатить {amount} отпускных денег. {name_and_date[0]}')


def print_attorney_letter(to_whom):
    global name_and_date
    print(f'На время отпуска в период {name_and_date[1]} моим заместителем назначается {to_whom}. {name_and_date[0]}')