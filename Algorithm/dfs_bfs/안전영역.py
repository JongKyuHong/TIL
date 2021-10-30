from collections import deque

def bfs(r, c, check):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and graph[nr][nc] >= check:
                visited[nr][nc] = 1
                q.append((nr, nc))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

delta = ((0,1),(0,-1),(1,0),(-1,0))
graph_min = min(map(min, graph))
graph_max = max(map(max, graph))
max_safe_area = graph_min
for safe_area in range(graph_min, graph_max+1):
    visited = [[0]*n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= safe_area and not visited[i][j]:
                bfs(i, j, safe_area)
                safe += 1
    if safe > max_safe_area:
        max_safe_area = safe
print(max_safe_area)

