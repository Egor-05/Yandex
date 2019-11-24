ma = 'a'
mi = 'ddddddddddddddddddddd'
while 1:
    word = input()
    if word == 'стоп':
        break
    if len(word) > len(ma):
        ma = word
    if len(word) < len(mi):
        mi = word
ma = set(ma)
mi = set(mi)
if mi < ma:
    print('ДА')
else:
    print('НЕТ')
