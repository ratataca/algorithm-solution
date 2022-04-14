T = int(input())
arr = []

for _ in range(T):
    x, y = map(int, input().split())
    arr.append([x, y])

arr = sorted(arr, key=lambda x : (x[0], x[1]))

for i in range(T):
    print(arr[i][0],arr[i][1])