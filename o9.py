def isvowel(letter):
    return letter.lower() in 'аеёиоуыэюя'


a = input().split()
c_b_l = 0
vowels = []
for i in a:
    if len(i) > 2:
        s = 0
        for j in i:
            if j.isupper() and isvowel(j):
                c_b_l += 1
                s += 1
            if isvowel(j):
                vowels.append(j)
        if s > 1:
            print('ошибка')
            exit(0)
res = []
if c_b_l == 0:
    print('ошибка')
else:
    if ''.join([vowels[i] for i in range(1, len(vowels), 2)]).isupper():
        res.append('ямб')
    elif ''.join([vowels[i] for i in range(0, len(vowels), 2)]).isupper():
        res.append('хорей')
    elif ''.join([vowels[i] for i in range(0, len(vowels), 3)]).isupper():
        res.append('дактиль')
    elif ''.join([vowels[i] for i in range(1, len(vowels), 3)]).isupper():
        res.append('амфибрахий')
    elif ''.join([vowels[i] for i in range(2, len(vowels), 3)]).isupper():
        res.append('анапест')
    else:
        print('не стихи')
if len(res) > 1:
    print('недостаточно информации')
elif len(res) == 1:
    print(res[0])
