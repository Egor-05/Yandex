p = [0] * 30000
a = input()
m = 0
s = 0
i = -1
while 1:
    i += 1
    if i >= len(a):
        break
    if a[i] == '+':
        if p[m] == 255:
            p[m] = 0
        else:
            p[m] += 1
    elif a[i] == '-':
        if p[m] == 0:
            p[m] = 255
        else:
            p[m] -= 1
    elif a[i] == '>':
        if m == 29999:
            m = 0
        else:
            m += 1
    elif a[i] == '<':
        if m == 0:
            m = 29999
        else:
            m -= 1
    elif a[i] == '.':
        print(p[m])
    elif a[i] == '[':
        if p[m] == 0:
            while 1:
                i += 1
                if a[i] == ']':
                    break
        else:
            while 1:
                i += 1
                if a[i] == '+':
                    p[m] = 255
                elif a[i] == '-':
                    p[m] = 0
                elif a[i] == '>':
                    if m == 29999:
                        m = 0
                    else:
                        m += 1
                elif a[i] == '<':
                    if m == 0:
                        m = 29999
                    else:
                        m -= 1
                elif a[i] == '.':
                    print(p[m])
                elif a[i] == ']':
                    break
                elif a[i] == '[':
                    while 1:
                        i += 1
                        if a[i] == '+':
                            p[m] = 255
                        elif a[i] == '-':
                            p[m] = 0
                        elif a[i] == '>':
                            if m == 29999:
                                m = 0
                            else:
                                m += 1
                        elif a[i] == '<':
                            if m == 0:
                                m = 29999
                            else:
                                m -= 1
                        elif a[i] == '.':
                            print(p[m])
                        elif a[i] == ']':
                            break
