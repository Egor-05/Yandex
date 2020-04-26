cache = []


def cached(func):
    def wrap(*args):
        global cache
        cache.append(func(*args))
        return func(*args)
    return wrap


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
print(cache)