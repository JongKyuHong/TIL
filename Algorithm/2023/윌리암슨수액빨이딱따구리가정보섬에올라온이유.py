from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
delta = ((0,1),(0,-1),(1,0),(-1,0))

q = deque()
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == '2':
            visited[i][j] = 1
            q.append((i, j))

def bfs(q):
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != '1' and not visited[nr][nc]:
                if graph[nr][nc] in ['3','4','5']:
                    return visited[r][c]
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0
ans = bfs(q)
if ans:
    print('TAK')
    print(ans)
else:
    print('NIE')

