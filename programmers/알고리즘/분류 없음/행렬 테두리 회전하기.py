def show(memo):
    for m in memo:
        for _m in m:
            print(_m, end="\t")
        print()
        
def rotate(x1, y1, x2, y2, memo, X, Y):
    _map = [[] for _ in range(Y)]
    for i in range(Y):
        _map[i] = memo[i][:]
    
    result_min = []
    # 1.    
    for nx in range(x1+1, x2+1):
        memo[y1][nx] = _map[y1][nx-1]
        result_min.append(_map[y1][nx-1])
            
    # 2.
    for ny in range(y1+1, y2+1):
        memo[ny][x2] = _map[ny-1][x2]
        result_min.append(_map[ny-1][x2])
    
    # 3.
    for nx in range(x2-1, x1-1, -1):
        memo[y2][nx] = _map[y2][nx+1]
        result_min.append(_map[y2][nx+1])
    
    # 4.
    for ny in range(y2-1, y1-1, -1):
        memo[ny][x1] = _map[ny+1][x1]
        result_min.append(_map[ny+1][x1])
    
    return min(result_min)
        
        

def solution(Y, X, queries):    
    
    # memo 만들기
    memo = []
    for i in range(Y):
        m = []
        for j in range(X):
            m.append(i * Y + j + 1)
        memo.append(m)
        
    # 쿼리로 부터 최소 값 구하기
    answer = []
    for y1, x1, y2, x2 in queries:
        y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1
        answer.append(rotate(x1, y1, x2, y2, memo, X, Y))
        
        show(memo)
        print("=" * 50)
        
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]


rows = 100
columns = 97
queries = [[1,1,100,97]]

print(solution(rows, columns, queries))