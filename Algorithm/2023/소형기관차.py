import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
limit = int(input())

S = [0]
value = 0
for l in lst:
    value += l
    S.append(value)

dp = [[0]*(N+1) for _ in range(4)]
for n in range(1, 4):
    for m in range(limit, N+1):
        dp[n][m] = max(dp[n][m-1], dp[n-1][m-limit] + S[m] - S[m-limit])
print(dp[3][N])
