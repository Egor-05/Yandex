way = input()
simvol = way[0]
spaces = 0
napravr = 0
napravl = 0
for i in range(len(way)):
    if 'V' == way[i]:
        if napravr > 0:
            print(' ' * spaces + simvol * napravr, end='')
            print()
            print(' ' * (spaces - 1), end='')
            print(simvol, end='')
        elif napravl > 0:
            print(' ' * spaces + simvol * napravl, end='')
            print()
            print(' ' * (spaces - 1), end='')
            print(simvol, end='')
    elif '>' == way[i]:
        napravr += 1
        spaces += 1
    elif '<' == way[i]:
        napravl += 1
        spaces -= 1
