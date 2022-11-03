import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

dp = [0]*(k+1)
for i in money:
    if k >= i:
        dp[i] += 1
        for j in range(i, k+1):
            dp[j] += dp[j-i]
print(dp[k])