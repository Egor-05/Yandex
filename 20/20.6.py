def print_document(pages):
    for i in pages:
        if i.split()[0] == 'Секретно':
            print('Дальнейшие материалы засекречены')
            return
        else:
            print(i)
    print('Напечатано без купюр')
