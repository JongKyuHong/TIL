n = int(input())
dp = [0]*1001
dp[1] = 1
dp[2] = 3

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    for i in range(3,n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    print(dp[n])