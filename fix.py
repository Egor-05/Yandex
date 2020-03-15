import pymorphy2


morph = pymorphy2.MorphAnalyzer()
word = morph.parse('бутылка')[0]
for i in range(99, 0, -1):
    print(f'В холодильнике {i} {word.make_agree_with_number(i).word} кваса.')
    print('Возьмём одну и выпьем.')
    if (i - 1) % 10 == 1 and i - 1 != 11:
        print(f'Осталась {i - 1} {word.make_agree_with_number(i - 1).word} кваса.')
    else:
        print(f'Осталось {i - 1} {word.make_agree_with_number(i - 1).word} кваса.')