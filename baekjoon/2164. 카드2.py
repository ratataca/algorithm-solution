from collections import deque

q = deque()
N = int(input())

for n in range(1, N+1):
    q.append(n)

while len(q) > 1:
    drop_v = q.popleft()
    insert_b = q.popleft()
    q.append(insert_b)

print(q[0])


