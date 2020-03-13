def print_statistics(arr):
    arr.sort()
    if len(arr) != 0:
        print(len(arr))
        print(sum(arr) / len(arr))
        print(float(min(arr)))
        print(float(max(arr)))
        if len(arr) % 2 == 1:
            print(float(arr[len(arr) // 2]))
        else:
            print((arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) / 2)
    else:
        for i in range(5):
            print(0)
