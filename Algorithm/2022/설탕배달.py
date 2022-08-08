n = int(input())

if n < 5:
    print(-1)
else:
    INF = float('inf')
    dp = [INF] * (n+1)

    dp[3] = 1
    dp[5] = 1

    for i in range(6,n+1):
        dp[i] = min(dp[i-3], dp[i-5]) + 1

    if dp[n] == INF:
        print(-1)
    else:
        print(dp[n])

