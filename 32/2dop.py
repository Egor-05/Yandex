import xlsxwriter


def export_check(texts):
    workbook = xlsxwriter.Workbook('res.xlsx')
    for text in texts.split('---'):
        worksheet = workbook.add_worksheet()
        text = text.strip('\n').split('\n')
        s = 0
        dct1 = {}
        for i in text:
            a = i.split('\t')
            if a[0] not in dct1:
                dct1[a[0]] = {}
            if a[0] in dct1 and float(a[1]) not in dct1[a[0]]:
                dct1[a[0]][float(a[1])] = 0
            dct1[a[0]][float(a[1])] += int(a[2])
        dct = {}
        for i in text:
            a = i.split('\t')
            if a[0] not in dct:
                dct[a[0]] = []
            if len(dct1[a[0]]) > len(dct[a[0]]):
                dct[a[0]].append((float(a[1]), int(dct1[a[0]][float(a[1])])))
        a = sorted(list(dct.keys()))
        pos = 0
        for i in range(len(a)):
            for j in dct[a[i]]:
                worksheet.write(pos, 0, a[i])
                worksheet.write(pos, 1, j[0])
                worksheet.write(pos, 2, j[1])
                x = f'=B{pos + 1}*C{pos + 1}'
                worksheet.write(pos, 3, x)
                pos += 1
        x = '=SUM(' + 'D' + '1' + ':' + 'D' + str(pos) + ')'
        worksheet.write(pos, 0, 'Итого')
        worksheet.write(pos, 3, x)
    workbook.close()


export_check('товар 1	100	5\n'
             'товар 2	200	6\n'
             'товар 3	7	500\n'
             'товар 1	5	23\n'
             'яблоко	10	10\n'
             'банан	20	15\n'
             'товар 1	100	5\n'
             'товар 2	200	6\n'
             'товар 3	7	500\n'
             'товар 1	5	23\n'
             'яблоко	10	10\n'
             'банан	20	15\n'
             '---'
             'товар 1	100	5\n'
             'товар 2	200	6\n'
             'товар 3	7	500\n'
             'товар 1	5	23\n'
             'яблоко	10	10\n'
             'груша	20	15\n'
             '---'
             'товар 1	100	5\n'
             'товар 2	200	6\n'
             'товар 3	7	500\n'
             'товар 1	100	5\n'
             'товар 2	200	6\n'
             'товар 3	7	500\n')
