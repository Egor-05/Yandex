stiles = {'01': 'ямб', '10': 'хорей', '100': 'дактиль', '010': 'амфибрахий', '001': 'анапест'}


def isvowel(letter):
    return letter.lower() in 'аеёиоуыэюя'


def find_ritm(s):
    for j in range(2, len(s) // 2 + 1):
        res = [s[c:c + j] for c in range(0, len(s), j) if c + j <= len(s)]
        if len(set(res)) == 1 and len(res) > 1:
            return res[0]
    return '0'


def check_poem(poem):
    listv = []
    for i in poem.split():
        vowels = ''.join(['1' if j.isupper() else '0' for j in i if isvowel(j)])
        if vowels.count('1') > 1:
            return 'ошибка'
        elif vowels != '':
            listv.append(vowels)
    listv = ''.join(listv)
    if listv.count('1') == 0:
        return 'ошибка'
    ritm = find_ritm(listv)
    if ritm in stiles:
        return stiles[ritm]
    elif '1' not in ritm:
        return 'не стихи'
    else:
        return 'недостаточно информации'


def tests():
    print(check_poem('мАма мЫла рАму') == 'хорей')
    print(check_poem('в магазИне закОнчилась едА') == 'не стихи')
    print(check_poem('Буря мглою небо кроет') == 'ошибка')
    print(check_poem('смотрЮ и Я, как бЫ живОй') == 'ямб')
    #  print(check_poem('в песчАных степЯх аравИйской землИ три гОрдые пАльмы высОко рослИ') == 'амфибрахий')
    print(check_poem('в песчАных степЯх аравИйской землИ') == 'амфибрахий')
    print(check_poem('три гОрдые пАльмы высОко рослИ') == 'амфибрахий')
    print(check_poem('ПрозвучАло над Ясной рекОю,') == 'анапест')
    print(check_poem('ПрозвенЕло в помЕркшем лугУ,') == 'анапест')
    print(check_poem('ПрокатИлось над рОщей немОю,') == 'анапест')
    print(check_poem('ЗасветИлось на тОм берегУ.') == 'анапест')
    print(check_poem('кАк хорошО ты, о мОре ночнОе,-') == 'дактиль')
    print(check_poem('ЗдЕсь лучезАрно, там сИзо - темнО...') == 'дактиль')
    print(check_poem('В лУнном сиЯнии, слОвно живОе,') == 'дактиль')
    print(check_poem('ХОдит и дЫшит, и блЕщет онО.') == 'дактиль')
    print(check_poem('А А А А А А А А А А А А') == 'недостаточно информации')
    print(check_poem('АААААААААААА') == 'ошибка')
    print(check_poem('аааааааааааааа') == 'ошибка')
    print(check_poem('ааааА ааааА ааааА ааааА') == 'недостаточно информации')
    print(check_poem('ааарпугпацугапагшцуаауцУ рвшгуацргаА') == 'не стихи')
    print(check_poem('Аа А Аа А') == 'недостаточно информации')
    print(check_poem('Вот хОлм лесИстый, нАд котОрым чАсто') == 'ямб')


# print(check_poem(input()))
tests()
