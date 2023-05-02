import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]
times = []
importance = []
for _ in range(K):
    a, b = map(int, input().split())
    importance.append(a)
    times.append(b)

for i in range(1, K+1):
    for j in range(1, N+1):
        if times[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-times[i-1]]+importance[i-1], dp[i-1][j])

print(dp[K][N])
