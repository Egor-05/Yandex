def bf(mest, command):
    if command == '+':
        if p[mest] == 255:
            p[mest] = 0
        else:
            p[mest] += 1
    elif command == '-':
        if p[mest] == 0:
            p[mest] = 255
        else:
            p[mest] -= 1
    elif command == '>':
        if mest == 29999:
            mest = 0
        else:
            mest += 1
    elif command == '<':
        if mest == 0:
            mest = 29999
        else:
            mest -= 1
    elif command == '.':
        print(p[mest])
    return mest


p = [0] * 30000
a = input()
m = 0
s = 0
i = -1
while 1:
    i += 1
    if a[i] == '[':
        if p[m] == 0:
            while 1:
                i += 1
                if a[i] == ']':
                    i += 1
                    break
        else:
            s = 0
            while 1:
                s += 1
                if a[i] == ']':
                    break
    m = bf(m, a[i])



            while a[i] != ']':
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
                elif a[i] == '[':
                    while a[i] != ']':
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
