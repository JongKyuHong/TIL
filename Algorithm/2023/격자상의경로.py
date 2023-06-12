import sys
input = sys.stdin.readline
delta = ((0, 1),(1, 0))

N, M, K = map(int, input().split())
if K == 0:
    dp = [[1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1])
    exit()
r = K//M if K%M != 0 else K//M-1# 행 
c = K%M-1 if K%M != 0 else M-1# 열33  
dp = [[1]*(c+1) for _ in range(r+1)]
for i in range(r+1):
    for j in range(c+1):
        if i == 0 or j == 0:
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
ans = dp[-1][-1]
dp = [[1]*(M-c) for _ in range(N-r)]
for i in range(N-r):
    for j in range(M-c):
        if i == 0 or j == 0:
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(ans*dp[-1][-1])