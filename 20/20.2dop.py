def palindrome(pal):
    pal = pal.replace(' ', '').lower()
    rp = pal[::-1]
    if pal == rp:
        return 'Палиндром'
    else:
        return 'Не палиндром'
