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


def bfstr(mest, strcom):
    if '[' in strcom:
        mest = pr(mest, strcom)
    else:
        for i in strcom:
            mest = bf(mest, i)
    return mest


def pr(mest, stri):
    levels = {'open': [], 'close': []}
    c = 0
    for i in range(len(stri)):
        if stri[i] == '[':
            c += 1
            if c == 1:
                levels['open'].append(i)
        elif stri[i] == ']':
            if c == 1:
                levels['close'].append(i)
            c -= 1
    mest = bfstr(mest, stri[:levels['open'][0]])
    for i in range(len(levels['open'])):
        while p[mest] != 0:
            mest = bfstr(mest, stri[levels['open'][i] + 1:levels['close'][i]])
        if i + 1 < len(levels['open']):
            mest = bfstr(mest, stri[levels['close'][i]:levels['open'][i + 1]])
    mest = bfstr(mest, stri[levels['close'][-1] + 1:])
    return mest


p = [0] * 30000
a = input()
bfstr(0, a)
