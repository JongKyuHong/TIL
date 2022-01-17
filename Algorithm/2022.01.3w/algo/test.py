from collections import deque
n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1

delta = ((0,1),(0,-1),(1,0),(-1,0))
visited = [[0]*m for _ in range(n)]
v = 0
def bfs(r, c):
    global v
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    v += 1
    while q:
        r, c  = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr,nc))
                v += 1
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i,j)
            result = max(result, v)
            v = 0
print(result)