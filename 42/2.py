def check_password(test):
    def wrap(*args):
        n = input('Введите пароль')
        if n != '123':
            return 'В доступе отказано'
        return test(*args)
    return wrap


@check_password
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))