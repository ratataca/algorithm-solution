from collections import deque

N = int(input())
M = int(input())

node_map = []
edges = []

for _ in range(N + 1):
    node_map.append([0 for n in range(N + 1)])

for _ in range(M):
    edges.append([int(n) for n in input().split()])

for x, y in edges:
    node_map[x][y] = node_map[y][x] = 1


bfs_visited = [False] * (N + 1)

def bfs(V):
    q = deque([V])
    cnt = -1
    while q:
        V = q.popleft()

        if bfs_visited[V]:
            continue
        cnt += 1
        bfs_visited[V] = True

        for i in range(1, N + 1):
            if bfs_visited[i] == False and node_map[V][i] == 1:
                q.append(i)
    return cnt

print(bfs(V=1))
