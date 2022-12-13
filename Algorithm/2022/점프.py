import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        value = graph[i][j]
        if value == 0:
            continue
        if i + value < n:
            dp[i+value][j] += dp[i][j]
        if j + value < n:
            dp[i][j+value] += dp[i][j]

print(dp[n-1][n-1])