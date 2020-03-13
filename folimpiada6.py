from random import sample


elems = ['2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r',
         't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
         'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y',
         'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
         'X', 'C', 'V', 'B', 'N', 'M']


def generate_password(m):
    while 1:
        prov1 = False
        prov2 = False
        prov3 = False
        a = ''.join(sample(elems, m))
        for i in a:
            if ord('A') <= ord(i) <= ord('Z'):
                prov1 = True
            if i.isdigit():
                prov2 = True
            if ord('a') <= ord(i) <= ord('z'):
                prov3 = True
        if prov1 and prov2 and prov3:
            break
    return a


def main(n, m):
    a = []
    for i in range(n):
        a1 = generate_password(m)
        while a1 in a:
            a1 = generate_password(m)
        a.append(a1)
    return a
