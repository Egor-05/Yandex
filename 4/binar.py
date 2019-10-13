left = 0
right = 1000
answer = None
while answer != "=":
    answer = input()
    if answer == "=":
        print("Я угадал!")
        break
    elif answer == "<":
        left = (left + right) // 2
        print(left)
    elif answer == ">":
        right = (right - left) // 2 + left
        print(right)