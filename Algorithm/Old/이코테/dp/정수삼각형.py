n = int(input())
dp = [[0]*i for i in range(1,n+1)]
for i in range(n):
    listn = list(map(int, input().split()))
    if i == 0:
        dp[0][0] = listn[0]
    else:
        for j in range(i+1):
            if j == 0:
                dp[i][j] = listn[j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = listn[j] + dp[i-1][j-1]
            else:
                dp[i][j] = listn[j] + max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[n-1]))

