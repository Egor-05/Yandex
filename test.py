from datetime import datetime as dt


def dec(func):
    def x(*args):
        a = dt.now()
        b = func(*args)
        print(dt.now() - a)
        return b
    return x


@dec
def func(string):
    return string * 2


@dec
def func1(t1, t2):
    return t1 + t2


print(func(1))
print(func1(1, 1))