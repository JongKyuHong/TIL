import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [[0]*2 for _ in range(302)]
dp[1][0] = stairs[0]
if N > 2:
    dp[2][0] = stairs[1]
    dp[2][1] = stairs[0] + stairs[1]

    for i in range(3, N+1):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i-1]
        dp[i][1] = max(dp[i-2][0], dp[i-2][1], dp[i-1][0]) + stairs[i-1]

print(max(dp[N][0], dp[N][1]))