def solution(m, n, puddles):
    answer = 0
    
    VISITABLE = 0
    PUDDLE = 10000
        
    # MAP 만들기
    map = [[0 for _ in range(m + 1)] for col in range(n + 1)]
            
        
    # 웅덩이
    for x, y in puddles:
        map[y][x] = PUDDLE
    
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            
            if x == 1 and y == 1:
                continue
            
            if map[y][x] == PUDDLE:
                continue
            
            if y - 1 == 0 and map[y][x - 1] != PUDDLE:
                map[y][x] = map[y][x - 1] + 1
            
            elif x - 1 == 0 and map[y][x - 1] != PUDDLE:
                map[y][x] = map[y- 1][x] + 1
            
            else:
                map[y][x] = min(map[y][x - 1], map[y - 1][x]) + 1
    
    result = min(map[n][m - 1], map[n - 1][m]) % 1000000007
    print(result)
    return result