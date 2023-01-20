import sys
input = sys.stdin.readline


nums = []
max_n = 0
for _ in range(int(input())):
    n, m = map(int, input().split())
    nums.append([n, m])
    max_n = max(max_n, n)

dp = [[0 for _ in range(max_n+1)] for _ in range(max_n+1)]
dp[1][1] = 1
if max_n > 1:
    dp[2][1] = 1
    dp[2][2] = 1
if max_n > 2:
    dp[3][1] = 1
    dp[3][2] = 2
    dp[3][3] = 1

for i in range(4, max_n+1):
    for j in range(1, i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1])%1000000009

for num in nums:
    print(dp[num[0]][num[1]])