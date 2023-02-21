from collections import deque
import sys
input = sys.stdin.readline

N, H, D = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
x,y = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'S':
            x, y = i, j
delta = ((0,1),(0,-1),(1,0),(-1,0))
q = deque()
q.append((x,y,0,0,H))
visited[x][y] = H
while q:
    r, c, dura, val, health  = q.popleft()
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if 0 <= nr < N and 0 <= nc < N:
            if graph[nr][nc] == 'E':
                print(val+1)
                exit()
            d = dura
            h = health
            if graph[nr][nc] == 'U':
                d = D
            if d == 0:
                h -= 1
            else:
                d -= 1
            if h == 0:
                continue
            if visited[nr][nc] < h:
                visited[nr][nc] = h
                q.append((nr, nc, d, val+1, h))
print(-1)