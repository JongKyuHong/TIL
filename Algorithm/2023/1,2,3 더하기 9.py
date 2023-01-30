import sys
input = sys.stdin.readline

max_n = 0
nums = []

dp = [[0]*(1001) for _ in range(1001)]
MOD = 1000000009
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1
for i in range(4, 1001):
    for j in range(2, i+1):
        dp[i][j] += (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD

for _ in range(int(input())):
    n, m = map(int, input().split())
    sum = 0
    for i in range(1, m+1):
        sum = (sum+dp[n][i])%MOD
    print(sum)
