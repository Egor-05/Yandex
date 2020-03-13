def partial_sums(*arr):
    na = []
    for i in range(0, len(arr) + 1):
        na.append(sum(arr[0:i]))
    return na