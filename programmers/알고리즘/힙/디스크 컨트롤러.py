import heapq

def solution(jobs):
    minHeap = []
    time = 0
    result = 0
    
    jobs = sorted(jobs)
    cnt = 0
    len_jobs = len(jobs)
    visited = [False] * len_jobs

    while cnt < len_jobs:
        # 지금 시간 보다 작은 job를 heapq 넣기
        for idx, value in enumerate(jobs):
            arrival_time, run_time = value[0], value[1]
            if arrival_time <= time and visited[idx] == False:
                heapq.heappush(minHeap, [run_time, arrival_time])
                visited[idx] = True
        

        # 최신에 대한 1개에 대한 연산진행
        if len(minHeap) > 0:
            # 연산 끝난거 heapq 제거
            run_time, arrival_time= heapq.heappop(minHeap)
            waitting_time = time - arrival_time        
            time += (run_time + waitting_time)
            result += (run_time + waitting_time)
            cnt += 1
        else:
            time += 1
        
    
    return result // len_jobs

# print(solution(	[[0, 3], [0, 2], [0, 1]]))
print(solution([[0, 3], [10, 2], [11, 1]]))