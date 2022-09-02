from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c, val):
    q = deque()
    q.append((r, c))
    cnt = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and graph[nr][nc]:
                visited[nr][nc] = val
                cnt += 1
                q.append((nr, nc))
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
num = 0
v = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and visited[i][j] == -1:
            num += 1 
            visited[i][j] = num
            cnt = bfs(i, j, num)
            v = max(cnt, v)

print(num)
print(v)