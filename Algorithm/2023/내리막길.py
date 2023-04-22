import sys
input = sys.stdin.readline
delta = ((0, 1),(0,-1),(1,0),(-1,0))
def dfs(r, c):
    if r == 0 and c == 0:
        return 1
    if dp[r][c] == 0:
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < M and 0 <= nc < N and lst[r][c] < lst[nr][nc]:
                if dp[nr][nc]:
                    dp[r][c] += dp[nr][nc]
                else:
                    dp[r][c] += dfs(nr, nc)
    return dp[r][c]
M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
dp = [[0]*N for _ in range(M)]

print(dfs(M-1,N-1))
