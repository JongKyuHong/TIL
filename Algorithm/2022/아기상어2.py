from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1))

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
def bfs(r1, c1):
    global ans
    q = deque()
    visited = [[0]*m for _ in range(n)]
    q.append((r1,c1,0))
    visited[r1][c1] = 1
    while q:
        r, c, dist = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if graph[nr][nc] == 0:
                    visited[nr][nc] = dist+1
                    q.append((nr, nc, dist+1))
                else:
                    return dist+1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            ans = max(ans, bfs(i, j))
print(ans)