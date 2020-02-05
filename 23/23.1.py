def matrix(n=1, m=0, a=0):
    if not m:
        m = n
    return [[a] * m for i in range(n)]
