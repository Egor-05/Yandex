word1 = input()
word2 = input()
lletter = word1[-1]
if lletter == 'ь':
    lletter = word1[-2]
if lletter == word2[0]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
