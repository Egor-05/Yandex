n = int(input())
message = input()
for i in message:
    if not i.isalpha():
        print(i, end='')
        continue
    if ((ord(i) + n > 1071) and (ord(i) <= 1071)) or ((ord(i) + n > 1103) and (ord(i) <= 1103)):
        i = chr(ord(i) - 32)
    i = chr(ord(i) + n)
    print(i, end='')