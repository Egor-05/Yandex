name = ''


def polite_input(question):
    global name
    if name == '':
        print('Как вас зовут?')
        name = input()
    print(f'{name}, {question}')
    input()
