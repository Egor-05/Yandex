import math


def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


def smaller_root(p, q):
    return (-p - math.sqrt(discriminant(1, p, q))) / (2 * 1)


def larger_root(p, q):
    return (-p + math.sqrt(discriminant(1, p, q))) / (2 * 1)


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(f'{smaller_root(p,q)} {larger_root(p,q)}')


main()