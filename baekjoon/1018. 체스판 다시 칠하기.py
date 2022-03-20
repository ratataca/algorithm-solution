M, N = [int(n) for n in input().split()]
_map = [] 
for _ in range(M):
    _map.append([])
    for s in input():
        _map[-1].append(s)

repair = []
for y in range(M-7):
    for x in range(N-7):
        count1 = 0
        count2 = 0

        for i in range(y, y+8):
            for j in range(x, x+8):
                # 짝수일 때
                if (i + j) % 2 == 0:
                    if _map[i][j] == 'B':
                        count1 = count1 + 1
                    if _map[i][j] == 'W':
                        count2 = count2 + 1
                
                # 홀수일 때
                else:
                    if _map[i][j] == 'W':
                        count1 = count1 + 1
                    if _map[i][j] == 'B':
                        count2 = count2 + 1

        repair.append(count1)
        repair.append(count2)

print(repair)
print(min(repair))        
