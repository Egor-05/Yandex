left = 1
right = 1000
answer = None
tries = 0
print('Загадайте в уме число от ', left, ' до ', right, ' я попробую его угадать. '
      'Если я отгадаю верно, то поставьте знак =, если ваше число больше, то >,'
      ' если меньше, то <.')
print((right - left) // 2)
while answer != "=" and tries != 10:
    answer = input()
    if answer == ">":
        left = (left + right) // 2
        print(left)
    elif answer == "<":
        right = (right - left) // 2 + left
        print(right)
    tries += 1
if tries == 10:
    print("О нет, я проиграл:-(")
else:
    print("Ура, я угадал!!!")