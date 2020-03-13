def golden_ratio(i):
    dividend = 1
    divider = 1
    for j in range(i - 1):
        dividend, divider = dividend + divider, dividend
    print(dividend / divider)
