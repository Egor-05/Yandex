def spam(name, date, email, place='Москве'):
    return f'To: {email}\nЗдравствуйте, {name}!\n' \
           f'Были бы рады видеть вас на встрече начинающих программистов в {place}, ' \
           f'которая пройдет {date}.'
