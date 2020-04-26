def check_password(test):
    def wrap(*args):
        return test(*args)

    def none(*args):
        return None

    n = input('Введите пароль: ')
    if n != '123':
        print('В доступе отказано')
        return none
    return wrap


@check_password
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))