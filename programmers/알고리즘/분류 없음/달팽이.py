def show(memo):
    for m in memo:
        print(*m)


def solution(N):
    cnt = 1
    memo = [[0] * (N + 1) for _ in range(0, N+1)]
    
    show(memo)
    print("=" * 50)
    
    T = N // 2
    if T % 2 == 1:
        T -= 1
    y_check = 0
    for t in range(1, T+1):
        move = [[1, 0], [0, 1], [-1, -1]]
    
        dy, dx = move[0]
        sx, sy =  t, y_check
        for _ in range(N):
            nx = sx + dx
            ny = sy + dy

            if 0 <= nx < N + 1 and 0 < ny < N + 1 and memo[ny][nx] == 0:
                memo[ny][nx] = cnt
                cnt += 1
                sx = nx
                sy = ny


        show(memo)
        print("=" * 50)
        print(">>> 1. ", sx, sy)
        dy, dx = move[1]
        for _ in range(N-1):
            nx = sx + dx
            ny = sy + dy

            if 0 <= nx < N + 1 and 0 < ny < N + 1 and memo[ny][nx] == 0:
                memo[ny][nx] = cnt
                cnt += 1
                sx = nx
                sy = ny

        show(memo)
        print("=" * 50)
        print(">>> 2. ", sx, sy)
        dy, dx = move[2]
        for _ in range(N-2):
            nx = sx + dx
            ny = sy + dy

            if 0 <= nx < N + 1 and 0 < ny < N + 1 and memo[ny][nx] == 0:
                memo[ny][nx] = cnt
                cnt += 1
                sx = nx
                sy = ny

            show(memo)
            print("=" * 50)

        y_check += 2
        N = N - 1

    result = [] 
    for m in memo:
        for n in m:
            if n != 0:
                result.append(n)

    return result


n = 5
print(solution(n))