class PolynomialPlus:
    def __init__(self, koef):
        self.koef = koef

    def __call__(self, x):
        s = 0
        for i in range(len(self.koef)):
            s += self.koef[i] * pow(x, i)
        return s

    def __add__(self, other):
        st = []
        k = PolynomialPlus(st)
        if len(self.koef) < len(other.koef):
            m = len(self.koef)
        else:
            m = len(other.koef)
        for i in range(m):
            st.append(self.koef[i] + other.koef[i])
        if len(self.koef) > m:
            st += self.koef[m::]
        else:
            st += other.koef[m::]
        return st


p1 = [int(i) for i in input().split()]
z = input()
p2 = [int(i) for i in input().split()]
# print(f'p1: polynom of {len(p1) - 1} power')
# print(f'coefficients: {", ".join([str(i) for i in p1])}')
# print(f'p1: polynom of {len(p2) - 1} power')
# print(f'coefficients: {", ".join([str(i) for i in p2])}')
if z == '+':
    poly1 = PolynomialPlus(list(reversed(p1)))
    poly2 = PolynomialPlus(list(reversed(p2)))
    print(list(reversed(poly1 + poly2)))