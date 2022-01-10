#치즈
from collections import deque

m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0]*n for _ in range(m)]
    visited[0][0] = 1
    while q:
        r,c = q.popleft()
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < m and 0 <= nc < n:
                if visited[nr][nc] == 0:
                    if graph[nr][nc] >= 1:
                        graph[nr][nc] += 1
                    else:
                        visited[nr][nc] = 1
                        q.append((nr,nc))
time = 0
while 1:
    bfs()
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                cnt = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if cnt == 1:
        time += 1
    else:
        break
print(time)
    

