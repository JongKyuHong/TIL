import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*1000001
dp[0] = 0
dp[1] = 1
for i in range(2, 1000001):
    dp[i] = ((dp[i-1])%1000000007 + (dp[i-2])%1000000007)%1000000007
print(dp[N])