import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[0]*(N+1) for _ in range(M+1)]
max_v = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        if graph[i-1][j-1] == 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            max_v = max(max_v, dp[i][j])
print(max_v)