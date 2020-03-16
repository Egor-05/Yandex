import xlsxwriter
import sys


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()
    text = text.strip('\n').split('\n')
    for i in range(len(text)):
        worksheet.write(i, 0, (text[i].split('\t'))[0])
        worksheet.write(i, 1, float((text[i].split('\t'))[1]))
        worksheet.write(i, 2, int((text[i].split('\t'))[2]))
        x = f'=B{i + 1}*C{i + 1}'
        worksheet.write(i, 3, x)
    x = '=SUM(' + 'D' + '1' + ':' + 'D' + str(len(text)) + ')'
    worksheet.write(len(text), 0, 'Итого')
    worksheet.write(len(text), 3, x)
    workbook.close()


export_check(sys.stdin.read())