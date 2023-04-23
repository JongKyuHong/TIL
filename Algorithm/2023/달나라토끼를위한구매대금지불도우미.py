import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*100001
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1
for i in range(8, 100001):
    dp[i] = min(dp[i-1] + 1, dp[i-2] + 1, dp[i-5] + 1, dp[i-7]+1)
print(dp[N])