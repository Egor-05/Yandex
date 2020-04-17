class Polynomial:
    def __init__(self, koef):
        self.koef = list(reversed(koef))
        while len(self.koef) > 1 and self.koef[-1] == 0:
            del self.koef[-1]

    def __add__(self, other):
        st = []
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
        return Polynomial(list(reversed(st)))

    def __sub__(self, other):
        st = []
        if len(self.koef) < len(other.koef):
            m = len(self.koef)
        else:
            m = len(other.koef)
        for i in range(m):
            st.append(self.koef[i] - other.koef[i])
        if len(self.koef) > m:
            st += self.koef[m::]
        else:
            st += other.koef[m::]
        return Polynomial(list(reversed(st)))

    def __mul__(self, other):
        mtx = []
        for i in range(len(other.koef)):
            c = [0] * i
            for j in range(len(self.koef)):
                c.append(self.koef[j] * other.koef[i])
            mtx.append(c)
        st = mtx[-1]
        for i in range(len(mtx) - 2, -1, -1):
            for j in range(len(mtx[i])):
                st[j] += mtx[i][j]
        return Polynomial(list(reversed(st)))

    def __str__(self):
        return f'polynom of {len(self.koef) - 1} power\n'\
               f'coefficients: {", ".join(reversed([str(i) for i in self.koef]))}'


poly1 = Polynomial([int(i) for i in input().split()])
z = input()
poly2 = Polynomial([int(i) for i in input().split()])
print('p1:', poly1)
print('p2:', poly2)
if z == '+':
    res1 = poly1 + poly2
elif z == '-':
    res1 = poly1 - poly2
elif z == '*':
    res1 = poly1 * poly2
print('result:', res1)