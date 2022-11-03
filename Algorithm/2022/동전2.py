import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

INF = float('inf')
dp = [INF]*(k+1)
for i in money:
    if k >= i:
        dp[i] = 1
        for j in range(i, k+1):
            dp[j] = min(dp[j], dp[j-i]+1)

print(-1 if dp[k] == INF else dp[k])