from collections import deque
from collections import defaultdict
"""
BFS
1. Queue 가 없을때까지 돈다. -> 종료 조건

2. 다음 노드 확인해서 앞으로 갈 게 뭔지 확인, 큐에 넣어주는거 -> 입력 조건

3. 방문했는지 안했는지 여부

인접 리스트 포맷
l = {
    "a": [b, c, d],
    "b": [c, d, e]
}

인접 행렬 포맷
map = [
    [~~],
    [~~~],
]
"""

def bfs(visited, q, l_dict):
    while q:
        node = q.popleft()

        for n in l_dict[node]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = 1    


def solution(N, computers):
    l_dict = defaultdict(list)
    for idx, value in enumerate(computers):
        for jdx, v in enumerate(value):
            if v == 1 and idx != jdx:
                l_dict[idx+1].append(jdx+1)
    
    visited = [0] * (N + 1)
    visited[0] = 1

    q = deque([])
    answer = 0
    for idx, value in enumerate(visited):
        if value == 0:
            q.append(idx)
            bfs(visited, q, l_dict)
            answer += 1

    return answer





n = 3
computer = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computer = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	

print(solution(n, computer))































# from collections import deque
# VISITALBE = 1
# VISITED = 2

# def show(memo):
#     for m in memo:
#         print(*m)
        
# def bfs(_map, q):
#     N = len(_map)
    
#     while q:
#         node = q.popleft()

#         for idx, value in enumerate(_map[node]):
#             if value == VISITALBE:
#                 _map[node][idx] = VISITED
#                 _map[idx][node] = VISITED
#                 q.append(idx)

#             print("=" * 50)
#             show(_map)
        
#     return 1
                

# def solution(N, computers):
    
#     for y in range(N):
#         for x in range(N):
#             if x == y:
#                 computers[y][x] = 0
#     show(computers)

#     q = deque([])
#     answer = 0
#     for y in range(N):
#         for x in range(N):
#             if computers[y][x] == VISITALBE:
#                 q.append(y)
#                 answer += bfs(computers, q)    

#     return answer

# n = 3
# computer = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# # computer = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


# print(solution(n, computer))
