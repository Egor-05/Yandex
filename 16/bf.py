p = [0] * 30000
a = input()
m = 0
s = 0
for i in a:
    if i == '+':
        if p[m] == 255:
            p[m] = 0
        else:
            p[m] += 1
    elif i == '-':
        if p[m] == 0:
            p[m] = 255
        else:
            p[m] -= 1
    elif i == '>':
        if m == 29999:
            m = 0
        else:
            m += 1
    elif i == '<':
        if m == 0:
            m = 29999
        else:
            m -= 1
    elif i == '.':
        print(p[m])
    elif i == '[':
        while 1:
            if i == '+':
                p[m] = 255
            elif i == '-':
                p[m] = 255
            elif i == '>':
                if m == 29999:
                    m = 0
                else:
                    m += 1
            elif i == '<':
                if m == 0:
                    m = 29999
                else:
                    m -= 1
            elif i == '.':
                print(p[m])
            elif i == ']':
                break