while True:
    arr = [int(n) for n in input().split()]
    if sum(arr) == 0:
        break

    arr = sorted(arr)
    long = arr[2] * arr[2]
    shorts = (arr[0] * arr[0]) + (arr[1] * arr[1])

    if long == shorts:
        print('right')
    else:
        print("wrong")