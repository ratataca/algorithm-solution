arr = map(int, input().split())

check = 0 not in arr or 180 not in arr
if sum(arr) == 180 and check:
    print('P')
else:
    print('F')