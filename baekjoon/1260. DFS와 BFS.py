from collections import deque


"""
deque.append()
deque.popleft() : O(1)
deque.pop() O(1)
"""


# 정점이 여러개 -> 정점 번호가 작은것 먼저 방문
# 더이상 방문할 수 있는 점이 없는 경우 종료
# 1 ~ N

# N, M, V = 4, 5, 1#[int(n) for n in input().split()]
# edges = [
#     [1, 2],
#     [1, 3],
#     [1, 4],
#     [2, 4],
#     [3, 4]
# ]

# N, M, V = 5, 5, 3#[int(n) for n in input().split()]
# edges = [
#     [5, 4],
#     [5, 2],
#     [1, 2],
#     [3, 4],
#     [3, 1]
# ]

N, M, V = [int(n) for n in input().split(" ")]
edges = []
for _ in range(M):
    edges.append([int(n) for n in input().split(" ")])

node = [[0] * (N + 1) for _ in range(N + 1)]
for n1, n2 in edges:
    node[n2][n1] = node[n1][n2] = 1

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
    q = deque([V])

    while q:
        V = q.popleft()

        if bfs_visited[V]:
            continue

        print(V, end=" ")
        bfs_visited[V] = True

        for i in range(1, len(node[V])):
            if bfs_visited[i] == False and node[V][i] == 1:
                q.append(i)
    print()

dfs(V=V)
bfs(V=V)
