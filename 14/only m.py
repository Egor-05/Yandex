listm = input().split(';')
for i in range(len(listm)):
    listm1 = listm[i].split(',')
    e = []
    for j in listm1:
        if int(j) >= 1000000000:
            e.append(j)
    print(','.join(e))
