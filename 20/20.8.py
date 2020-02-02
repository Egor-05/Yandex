def password_level(pas):
    if len(pas) >= 6:
        nums = len([i for i in pas if i.isdigit()]) > 0
        if nums:
            if pas.isdigit():
                return 'Ненадежный пароль'
            else:
                if pas == pas.lower() or pas == pas.upper():
                    return 'Слабый пароль'
                else:
                    return 'Надежный пароль'
        else:
            if pas == pas.lower() or pas == pas.upper():
                return 'Ненадежный пароль'
            else:
                return 'Слабый пароль'
    else:
        return 'Недопустимый пароль'
