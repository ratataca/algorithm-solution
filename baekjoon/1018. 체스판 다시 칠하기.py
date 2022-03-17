def isChess(chess):
    
    for ch in chess:
        left = ch[0:8:2] 
        right = ch[1:8:2]
        

        print('=' * 40)


# M, N = [int(n) for n in input().split()]
# _map = [[s for s in input()] for _ in range(M)]

# print(_map)


M, N = 8, 8
_map = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

result = 100

for y in range(M):
    for x in range(N):
        if y + 8 <= M and x + 8 <= N:
            chess = _map[y:y+8][x:x+8]
            result = min(isChess(chess), result)
            

        
