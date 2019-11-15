a = input()
s = 0
ns = 0
for i in a:
    if ord('a') <= ord(i) >= ord('z'):
        s += 1
    elif i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9:
        s += 1
    elif ord(i) == ord('_'):
        s += 1
    else:
        ns = i
        break
if s == len(a):
    print('OK')
else:
    print('Неверный символ:', ns)
