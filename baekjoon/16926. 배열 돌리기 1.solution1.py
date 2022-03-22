import sys
input = sys.stdin.readline

def rotate():
    # 테두리 사각형을 회전할 횟수
    check = min(N, M) // 2

    for cnt in range(check):
        n_max = N - 1 - cnt
        m_max = M - 1 - cnt

        tmp = map[cnt][cnt]

        # 위쪽 왼 <- 오
        for i in range(cnt, m_max):
            map[cnt][i] = map[cnt][i + 1]
            
        # 오른쪽 아래 <- 위
        for i in range(cnt, n_max):
            map[i][m_max] = map[i + 1][m_max]

        # 왼쪽 왼 -> 오
        for i in range(m_max, cnt, -1):
            map[n_max][i] = map[n_max][i - 1]

        # 왼쪽 위 -> 아래
        for i in range(n_max, cnt, -1):
            map[i][cnt] = map[i - 1][cnt]

        map[cnt+1][cnt] = tmp


N, M, T = [int(n) for n in input().split()]
map = [[int(n) for n in input().split()] for _ in range(N)]

while True:
    if T == 0:
        break 
    
    rotate()
    T -= 1

for m in map:
    print(' '.join([str(n) for n in m]))