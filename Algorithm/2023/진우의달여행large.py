import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf')]*M for _ in range(N)] for _ in range(3)]

for i in range(3):
    for j in range(M):
        dp[i][0][j] = lst[0][j]

for i in range(N):
    for j in range(M):
        for k in range(3):
            if k == 0:
                dp[k][i][j] = min(dp[k][i][j], dp[1][i-1][j]+lst[i][j])
                if j > 0:
                    dp[k][i][j] = min(dp[k][i][j], dp[2][i-1][j-1]+lst[i][j])
            elif k == 1:
                if j < M-1:
                    dp[k][i][j] = min(dp[k][i][j], dp[0][i-1][j+1]+lst[i][j])
                if j > 0:
                    dp[k][i][j] = min(dp[k][i][j], dp[2][i-1][j-1]+lst[i][j])
            else:
                dp[k][i][j] = min(dp[k][i][j], dp[1][i-1][j]+lst[i][j])
                if j < M-1:
                    dp[k][i][j] = min(dp[k][i][j], dp[0][i-1][j+1]+lst[i][j])

min_v = float('inf')
for i in range(3):
    for j in range(M):
        min_v = min(min_v, dp[i][N-1][j])
        #print(dp[i][N-1][j],'dd')
print(min_v)
