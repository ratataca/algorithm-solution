def isHansu(n):
    arr = [int(i) for i in n]
    if len(arr) > 1:
        interval = arr[1] - arr[0]

    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i]) != interval:
            return False
    return True


N = int(input())
cnt = 0

for i in range(1, N+1):
    if isHansu(str(i)):
        cnt += 1

print(cnt)