import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    S[i] %= 2
    for j in range(K+1):
        if S[i] == 0:
            dp[i][j] = dp[i-1][j] + 1
        if j != 0 and S[i]:
            dp[i][j] = dp[i-1][j-1]
res = []
for i in dp:
    res.append(i[K])
print(max(res))
