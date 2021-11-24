def self_num(n):
    arr = [int(i) for i in n]
    return int(n) + sum(arr)


arr = [0] * 10001
arr[0] = -1
for i in range(1, 10001):
    result = self_num(str(i))
    if result <= 10000:
        arr[result] = 1

for idx, num in enumerate(arr):
    if num == 0:
        print(idx)