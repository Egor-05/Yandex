a = int(input())
b = 1
print(b)
c = 1
print(c)
while b < a:
    b += c
    if b > a:
        break
    else:
        print(b)
    c += b
    if c > a:
        break
    else:
        print(c)