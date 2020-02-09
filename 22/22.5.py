def make_shades(alley, k):
    s = 0
    k1 = k
    for i in range(len(alley)):
        if k < 0:
            alley.reverse()
            k = -k
        if s == 0 and alley[i] != 0:
            s = k * alley[i] + 1
        if s != 0 and alley[i] != 0:
            if k * alley[i] + 1 > s:
                s = k * alley[i] + 1
        if s != 0:
            alley[i] += 1
            s -= 1
    tf = []
    for i in alley:
        if i == 0:
            tf.append(False)
        else:
            tf.append(True)
    if k1 < 0:
        tf.reverse()
    return tf


def calculate_sunny_length(shades):
    return shades.count(False)


def main():
    k = int(input())
    alley = [int(i) for i in input().split()]
    if calculate_sunny_length(make_shades(alley, k)) < 10:
        print('Тени достаточно')
    else:
        print('Обгорел')

