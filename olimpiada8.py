green, red = [int(i) for i in input().split()]
P, V, A = [int(i) for i in input().split()]
if (P / V) % (green + red) < green:
    print('Pass')
else:
    S = V ** 2 / (A * 2)
    sectime = P / V + V / (2 * A)
    start_time = (red + green) - (sectime % (green + red))
    print('%.3f' % S, '%.3f' % start_time)
