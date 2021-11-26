from collections import deque

N, M, V = [int(n) for n in input().split()]
edges = []

for _ in range(M):
    edges.append([int(n) for n in input().split(" ")])

node = [[0] * (N + 1) for _ in range(N + 1)]

for n1, n2 in edges:
    node[n1][n2] = node[n2][n1] = 1

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

def dfs(V):
    stack = [V]
    while stack:
        V = stack.pop()

        if dfs_visited[V]:
            continue

        print(V, end=" ")
        dfs_visited[V] = True

        for i in range(len(node[V]) - 1, 0, -1):
            if dfs_visited[i] == False and node[V][i] == 1:
                stack.append(i)

    print()


def bfs(V):
    q = deque()

