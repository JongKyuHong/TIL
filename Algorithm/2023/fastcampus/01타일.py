import sys 
input = sys.stdin.readline

N = int(input())
dp = [0]*1000001
dp[1] = 1 # 1
dp[2] = 2 # 00 11
dp[3] = 3 # 100 001 111
dp[4] = 5 # 0011 0000 1001 1100 1111

for i in range(5, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%15746)