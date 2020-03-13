from sys import stdin


text = '''\tАрифметика для старших\tГеометрия в четырехмерье\tЭсперанто для начинающих
Пятёрка\t205\t300\t420
Академкнига\t500\t200\t250
Всё для школы\t350\t350\t350'''


def solve(text):
    data = list(map(lambda s: s.split('\t'), text.splitlines()))
    row = min(data[1:], key=lambda x: sum(map(int, x[1:])))
    res = map(lambda x: f'{x[0]}\t{x[1]}'.strip(), zip(data[0], row))
    return '\n'.join(res)


print(solve(text))
data = [i.split('\t') for i in stdin]
row = min(data[1:], key=lambda x: sum(map(int, x[1:])))
res = map(lambda x: f'{x[0]}\t{x[1]}'.strip(), zip(data[0], row))
print('\n'.join(res))
