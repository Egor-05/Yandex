fs = []
while 1:
    a = input()
    if a == '':
        break
    a = a.split(':')
    fs.append(a)
pwd = input().split(';')
for i in fs:
    for j in pwd:
        if i[1] == j:
            print(f'To: {i[0]}')
            print(f'{i[4].split(",")[0]}, ваш пароль слишком простой, смените его.')
