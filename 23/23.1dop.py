def encrypt_caesar(msg, shift=3):
    c = []
    for i in msg:
        if not i.isalpha() and ord('А') > ord(i) or ord(i) > ord('я'):
            c.append(i)
            continue
        elif i.islower() and ord(i) + shift > ord('я'):
            i = chr(ord(i) - 32)
        elif i.isupper() and ord(i) + shift > ord('Я'):
            i = chr(ord(i) - 32)
        i = chr(ord(i) + shift)
        c.append(i)
    return ''.join(c)


def decrypt_caesar(encrypted, shift=3):
    shift = -shift
    c = []
    for i in encrypted:
        if not i.isalpha() and ord('А') > ord(i) or ord(i) > ord('я'):
            c.append(i)
            continue
        elif i.islower() and ord(i) + shift < ord('а'):
            i = chr(ord(i) + 32)
        elif i.isupper() and ord(i) + shift < ord('А'):
            i = chr(ord(i) + 32)
        i = chr(ord(i) + shift)
        c.append(i)
    return ''.join(c)
