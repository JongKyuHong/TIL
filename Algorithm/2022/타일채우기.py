import sys
input = sys.stdin.readline

n = int(input())
if n % 2:
    print(0)
else:
    if n == 2:
        print(3)
    else:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[2] = 3
        idx = 0
        for i in range(4,n+1,2):
            dp[i] = dp[i-4]*2 + dp[i-2]*3
        
        print(dp[n])