def line(s, t):
    k, b = [float(i) for i in s.split('x')]
    x, y = [float(i) for i in t.split(';')]
    if k * x + b == y:
        print('True')
    else:
        print('False')
