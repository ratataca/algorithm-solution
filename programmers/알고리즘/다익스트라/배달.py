import heapq

def solution(N, road, K):
    answer = 0
    # 그래프 노드
    graph = [[] * (N + 1) for _ in range(N + 1)]
    print(graph)

    for s_n, e_n, w in road:
        graph[s_n].append([e_n, w])
        graph[e_n].append([s_n, w])
    print(graph)
    
    # 방문 표시
    INF = int(1e9)
    distance = [INF] * (N + 1)
    start_node = 1
    

    # 다익스트라
    q = []
    distance[start_node] = 0
    heapq.heappush(q, (0, start_node))
    
    while q:
        w_n, s_n = heapq.heappop(q)

        if distance[s_n] < w_n:
            continue

        for e_n, w in graph[s_n]:
            cost = w_n + w    
            if cost <= K and cost < distance[e_n]:
                distance[e_n] = cost
                heapq.heappush(q, (cost, e_n))
                answer += 1    
    return answer + 1


N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3


N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4


print("result : ", end='')
print(solution(N, road, K))