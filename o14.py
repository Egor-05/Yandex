import pymorphy2


morph = pymorphy2.MorphAnalyzer()
for i in range(99, 0, -1):
    word = morph.parse('бутылка')[0]
    ost = morph.parse('Осталось')[0]
    print(f'В холодильнике {i} {word.make_agree_with_number(i).word} кваса.')
    print('Возьмём одну и выпьем.')
    print(f'{ost.make_agree_with_number(i - 1).word} {i - 1} {word.make_agree_with_number(i - 1).word} кваса.')