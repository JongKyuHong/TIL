import sys 
input = sys.stdin.readline

input = sys.stdin.readline
N, S, M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [[] for _ in range(N+1)]

dp[0].append(S)

for i in range(1, N+1):
    for j in range(len(dp[i-1])):
        tmp = dp[i-1][j] - lst[i-1]
        if tmp not in dp[i] and tmp >= 0:
            dp[i].append(tmp)
        tmp = dp[i-1][j] + lst[i-1]
        if tmp not in dp[i] and tmp <= M:
            dp[i].append(tmp)
print(max(dp[N]) if dp[N] else -1)