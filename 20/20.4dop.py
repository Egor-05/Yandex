def catalan(n):
    if n > 1:
        res = ((2 * ((2 * n) - 1)) / (n + 1)) * catalan(n - 1)
        return int(res)
    return 1
