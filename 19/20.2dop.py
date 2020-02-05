def equation(first_point, second_point):
    first_pointx, first_pointy = [float(i) for i in first_point.split(";")]
    second_pointx, second_pointy = [float(i) for i in second_point.split(";")]
    k = 0.0
    b = 0.0
    if first_pointx != second_pointx
        if first_pointx != 0 or second_pointx != 0:
            if first_pointx != 0:
                k = float(first_pointy // first_pointx)
            elif second_pointx != 0:
                k = float(second_pointy // second_pointx)
            b = second_pointy - k * second_pointx
        print(k, b)


equation("4;6.9", "-5.2;6.9")
