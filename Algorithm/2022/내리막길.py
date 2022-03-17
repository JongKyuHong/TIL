def dfs(r, c):
    if r == 0 and c == 0:
        return 1
    if visited[r][c] == -1:
        visited[r][c] += 1
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < m and 0 <= nc < n:
                if graph[r][c] < graph[nr][nc]:
                    visited[r][c] += dfs(nr, nc)
    return visited[r][c]
                
delta = ((0,1),(0,-1),(1,0),(-1,0))
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)]
visited[0][0] = 1
result = dfs(m-1,n-1)
print(result)
