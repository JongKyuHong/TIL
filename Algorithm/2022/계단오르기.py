n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)
dp2 = [0] * (n+1)

if n > 2:
    dp[1] = stairs[1]
    dp2[1] = 1
    dp[2] = stairs[2]+stairs[1]
    dp2[2] = 2

    for i in range(3, n+1):
        dp[i] = max(stairs[i-1]+dp[i-3],dp[i-2]) + stairs[i]
    print(dp[n])
elif n == 1:
    print(stairs[1])
else:
    print(stairs[1]+stairs[2])