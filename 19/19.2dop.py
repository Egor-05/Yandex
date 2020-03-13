def equation(first_point, xy2):
    first_pointx = int(first_point.split(";")[0])
    first_pointy = int(first_point.split(";")[1])
    second_pointx = int(xy2.split(";")[0])
    second_pointy = int(xy2.split(";")[1])
    if first_pointx != 0 or first_pointy != 0:
        if first_pointx != 0:
            k = first_pointy // first_pointx
        elif second_pointx != 0:
            k = second_pointy // second_pointx
        b = second_pointy - k * second_pointx
        print(k, b)


equation("0;0", "0;4")
