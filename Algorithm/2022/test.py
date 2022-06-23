n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [([0]*m) for _ in range(n)]
delta = ((-1,0),(0,1),(1,0),(0,-1))
ans = 0
max_val = max(map(max, graph))

def dfs(r,c,idx,total):
    global ans
    if ans >= total + max_val * (3-idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if idx == 1:
                    visited[nr][nc] = 1
                    dfs(r, c, idx+1, total+graph[nr][nc])
                    visited[nr][nc] = 0
                visited[nr][nc] = 1
                dfs(nr, nc, idx+1, total+graph[nr][nc])
                visited[nr][nc] = 0

for r in range(n):
    for c in range(m):
        visited[r][c] = 1
        dfs(r, c, 0, graph[r][c])
        visited[r][c] = 0