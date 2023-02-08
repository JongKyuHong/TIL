from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c):
    q = deque()
    q.append((r,c))
    o, v = 0, 0
    if graph[r][c] == 'o':
        o += 1
    elif graph[r][c] == 'v':
        v += 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and graph[nr][nc] != '#':
                visited[nr][nc] = 1
                q.append((nr, nc))
                if graph[nr][nc] == 'o':
                    o += 1
                elif graph[nr][nc] == 'v':
                    v += 1
    return [o, v]

R, C = map(int, input().split())
wolf, sheep = 0, 0
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and not visited[i][j]:
            visited[i][j] = 1
            o, v = bfs(i, j)
            if o > v:
                sheep += o
            else:
                wolf += v
print(sheep, wolf)