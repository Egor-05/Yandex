def ask_password(login, password, success, failure):
    l_o_c = ''.join([i for i in login if i not in 'aeiouy' and i.isalpha()])
    p_o_c = ''.join([i for i in password if i not in 'aeiouy' and i.isalpha()])
    if len([i for i in password if i in 'aeiouy']) == 3 and l_o_c == p_o_c:
        return success(login)
    elif len([i for i in password if i in 'aeiouy']) != 3 and l_o_c == p_o_c:
        return failure(login, 'Wrong number of vowels')
    elif len([i for i in password if i in 'aeiouy']) == 3 and l_o_c != p_o_c:
        return failure(login, 'Wrong consonants')
    else:
        return failure(login, 'Everything is wrong')


def main(login, password):
    ask_password(login.lower(), password.lower(),
                 lambda login: print(f'Привет, {login}!'),
                 lambda login, err: print(f'Кто-то пытался притвориться пользователем '
                                          f'{login}, но в пароле допустил ошибку: {err.upper()}.'))
