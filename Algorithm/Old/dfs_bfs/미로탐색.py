from collections import deque

def bfs(r, c):
    global res
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if nr < 0 or nc < 0 or nr >= n or nc >= m or not array[nr][nc]:
                continue
            if visited[nr][nc] > visited[r][c] + 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))

delta = ((0,1),(0,-1),(1,0),(-1,0))
n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
INF = float('inf')
visited = [[INF]*m for _ in range(n)]
res = 10*6 + 1
visited[0][0] = 1
bfs(0,0)
print(visited[n-1][m-1])
