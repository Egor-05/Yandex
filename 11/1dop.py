s = input()
n = int(input())
letter = input()
if (0 < n <= len(s)) and letter == s[n - 1] and len(letter) == 1:
    print('ДА')
elif (0 < n <= len(s)) and letter != s[n - 1] and len(letter) == 1:
    print('НЕТ')
else:
    print('ОШИБКА')