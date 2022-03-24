from collections import deque

T = int(input())

while True:
    if T == 0:
        break

    _, target = map(int, input().split())
    arr = map(int, input().split())

    q = deque()
    max_arr = deque()
    for idx, value in enumerate(arr):
        q.append([idx, value])
        max_arr.append(value)
        
    cnt = 0
    while q:
        idx, value = q.popleft()
        cur_value = max_arr.popleft()

        if len(q) != 0 and value < max(max_arr):
            q.append([idx, value])
            max_arr.append(cur_value)
        else:
            cnt += 1
            if idx == target:
                break
    print(cnt)
    T -= 1