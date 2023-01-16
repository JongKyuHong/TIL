from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(M) for _ in range(N)]
dp[0][0] = area[0][0]
for i in range(N-1):
    dp[i+1][0] = dp[i][0]+area[i+1][0]
for i in range(M-1):
    dp[0][i+1] = dp[0][i]+area[0][i+1]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i][j], dp[i-1][j]+area[i][j], dp[i][j-1]+area[i][j])
print(dp[N-1][M-1])
