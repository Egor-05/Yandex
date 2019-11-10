way = input()
simvol = way[0]
spaces = 0
napravr = 0
nway = input()
sign = way[0]
for i in range(len(way)):
    if 'V' == way[i]:
        print()
        print(sign,  end='')
        continue
    elif '>' or '<' == way[i]:
        print(sign, end='')
        continue
    else:
        print(sign)