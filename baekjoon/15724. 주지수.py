## 질문
# 진심 두개의 차이가 뭔데..

'''
4 4
9 14 29 7
1 31 6 13
21 26 40 16
8 38 11 23
3
1 1 3 2
1 1 1 4
1 1 4 4
'''

import sys
input = sys.stdin.readline

N, M = [int(n) for n in input().split()]
area = [[int(n) for n in input().split()] for _ in range(N)]

K  = int(input())

dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for y1, x1, y2, x2 in area:
    print(dp[y2][x2] - dp[y1-1][x1] - dp[y1][x1-1] + dp[y1-1][x1-1])


# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# area = [list(map(int,input().split())) for _ in range(n)]

# dp = [[0]*(m+1) for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# for _ in range(int(input())):
#     x,y,i,j = map(int,input().split())
#     print(dp[i][j] - dp[x-1][j] - dp[i][y-1] + dp[x-1][y-1])