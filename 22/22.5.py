def make_shades(alley, k):
    s = 0
    for i in range(len(alley)):
        if k >= 0:
            if s == 0 and alley[i] != 0:
                s = k * alley[i] + 1
            if s != 0 and alley[i] != 0:
                if k * alley[i] + 1 > s:
                    s = k * alley[i] + 1
            if s != 0:
                alley[i] += 1
                s -= 1
        else:
            if s == 0 and alley[i] != 0:
                s = k * alley[i] + 1
                for j in range(i, 0):
                    alley[j] += 1
                    s -= 1
    tf = []
    for i in alley:
        if i == 0:
            tf.append(False)
        else:
            tf.append(True)
    return tf


def calculate_sunny_length(shades):
    return shades.count(False)


def main():
    k = int(input())
    alley = [int(i) for i in input().split()]
    if calculate_sunny_length(make_shades(alley, k)) <= 10:
        print('Тени достаточно')
    else:
        print('Обгорел')


print(make_shades([0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0], -1))