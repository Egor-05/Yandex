from random import choice


elems = ['2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r',
         't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
         'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y',
         'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
         'X', 'C', 'V', 'B', 'N', 'M']


def generate_password(m):
    return ''.join(list(choice(elems, k=m)))


def main(n, m):
    a = []
    for i in range(n):
        a1 = generate_password(m)
        while a1 in a:
            a1 = generate_password(m)
        a.append(a1)
    return a


print(main(3, 4))