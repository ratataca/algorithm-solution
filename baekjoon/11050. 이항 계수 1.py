N, K = map(int, input().split())
arr = [1] * (N + 1)

for i in range(1, len(arr)):
    arr[i] = arr[i - 1] * i

print(int(arr[N] / (arr[K] * arr[N-K])))