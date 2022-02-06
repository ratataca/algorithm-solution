# BFS 
# 인접 리스트를 활용.
from collections import deque

def bfs(q, relation, visited):
    
    cnt = 0
    while q:
        node1, node2, deep = q.popleft()
        
        for n1, n2 in relation:
            if n1 == node2 and deep < 3:
                q.append([n1, n2, deep + 1])
                cnt += 1

    return cnt - 1


# N = int(input())
# M = int(input())
# relation = []

# for _ in range(M):
#     relation.append([int(n) for n in input().split()])

relation=[
    [1, 2],
    [1, 3],
    [3, 4],
    [3, 2],
    [4, 5]
]

relation = sorted(relation, key=lambda x : x[0])

# Definition of Queue
q = deque()

for node1, node2 in relation:
    if node1 == 1:
        q.append([node1, node2, 1])

if len(q) == 0:
    print(0)
else:
    visited = [False] * M
    print(bfs(q, relation, visited))