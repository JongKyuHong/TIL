from collections import deque

delta = ((0,1),(0,-1),(1,0),(-1,0))
def dijkstra(r, c):
    q = deque()
    q.append((r,c))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    if graph[nr][nc] > graph[r][c]:
                        visited[nr][nc] = visited[r][c] + graph[nr][nc] - graph[r][c] + 1
                    else:
                        visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                else:
                    if graph[nr][nc] > graph[r][c]:
                        if visited[nr][nc] > visited[r][c] + graph[nr][nc] - graph[r][c] + 1:
                            visited[nr][nc] = visited[r][c] + graph[nr][nc] - graph[r][c] + 1
                            q.append((nr, nc))
                    else:
                        if visited[nr][nc] > visited[r][c] + 1:
                            visited[nr][nc] = visited[r][c] + 1
                            q.append((nr, nc))

for T in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 0
    dijkstra(0, 0)
    print(f'#{T+1} {visited[n-1][n-1]}')