def solution(people, limit):
    lenght = len(people)
    visited = [0] * lenght
    answer = 0
    
    for i in range(lenght):
        max_value = []
        if visited[i] == 1:
            continue
            
        visited[i] = 1
        for j in range(i+1, lenght):
            standard = limit - people[i]
            if people[j] <= standard and visited[j] == 0:
                max_value.append([people[j], j])
        
        if len(max_value) > 0:
            max_value.sort()
            visited[max_value[-1][1]] = 1
        answer += 1
    
    return answer


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))