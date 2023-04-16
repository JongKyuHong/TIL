import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] > graph[r][c]:
            dp[r][c] = max(dp[r][c], dfs(nr,nc) + 1)

    return dp[r][c]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dfs(i, j)

max_v = 0
for i in range(n):
    max_v = max(max_v, max(dp[i]))

print(max_v+1)