import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*(M+1) for _ in range(N+1)]
cnt = 0
def dfs(r, c):
    global cnt

    if (c, r) == (1, N+1):
        cnt += 1
        return
    
    if c == M:
        nc, nr = 1, r+1
    else:
        nc, nr = c+1, r
    
    dfs(nr, nc)

    if graph[r-1][c] == 0 or graph[r-1][c-1] == 0 or graph[r][c-1] == 0:
        graph[r][c] = 1
        dfs(nr ,nc)
        graph[r][c] = 0

dfs(1, 1)
print(cnt)