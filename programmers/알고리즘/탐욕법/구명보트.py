def solution(people, limit):
    length = len(people)
    visited = [0] * length
    answer = 0
    
    for i in range(length):
        max_value = []
        if visited[i] == 1:
            continue
            
        visited[i] = 1
        for j in range(i+1, length):
            
            standard = limit - people[i]
            print(">>", j, standard)
            if people[j] <= standard and visited[j] == 0:
                max_value.append([people[j], j])
        
        print(i, j, max_value)
        
        if len(max_value) > 0:
            max_value.sort()
            visited[max_value[-1][1]] = 1
        answer += 1
    
    return answer


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))