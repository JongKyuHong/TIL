from collections import deque

delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs():
    visited = [[0] * n for _ in range(m)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    cnt = 0
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                if graph[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
                elif graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    cnt += 1
                    visited[nr][nc] = 1
    cheese.append(cnt)
    return cnt
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
cheese = []

time = 0
while 1:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(cheese[-2])