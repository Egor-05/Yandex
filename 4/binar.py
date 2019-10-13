left = 1
right = 1000
answer = None
print('Загадайте в уме число от ', left, ' до ', right, ' я попробую его угадать. Если я отгадаю верно, то поставьте'
      ' знак =, если ваше число больше, то >, если меньше, то <.')
print((right + left) // 2)
while answer != "=":
    answer = input()
    if answer == ">":
        left = (left + right) // 2
        print(left)
    elif answer == "<":
        right = (right - left) // 2 + left
        print(right)
print("Я угадал!")