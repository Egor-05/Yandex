a = int(input())
booltf = False
s1 = ''
for i in range(a):
    c = input()
    c_wo_b_s = c.lstrip()
    num_of_s = len(c) - len(c_wo_b_s)
    c1 = c_wo_b_s.split("'")
    c2 = []
    res_str = ''
    for j in c1:
        if len(j) >= 1:
            if j[-1] == '\\' and (len(j) >= 2 and j[-2] != '\\'):
                res_str += j + '\''
            else:
                res_str += j
                c2.append(res_str)
                res_str = ''
    c3 = []
    for j in range(len(c2)):
        if ('#' in c2[j]) and (j % 2 == 0):
            c3.append(c2[j].split('#')[0])
            break
        else:
            c3.append(c2[j])
    for j in range(len(c3)):
        if j % 2 == 0:
            while '  ' in c3[j]:
                c3[j] = c3[j].replace('  ', ' ')
    for j in range(1, len(c3), 2):
        c3[j] = "'" + c3[j] + "'"
    print(' ' * num_of_s + ''.join(c3))
