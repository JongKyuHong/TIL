for T in range(int(input())):
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6
    for i in range(4, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2] + dp[i-3]
    print(f'#{T+1} {dp[n]}')