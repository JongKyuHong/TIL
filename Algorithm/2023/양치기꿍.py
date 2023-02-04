from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c):
    q = deque()
    q.append((r,c))
    v, k = 0, 0
    if graph[r][c] == 'v':
        v += 1
    elif graph[r][c] == 'k':
        k += 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != '#' and not visited[nr][nc]:
                visited[nr][nc] = 1
                if graph[nr][nc] == 'v':
                    v += 1
                elif graph[nr][nc] == 'k':
                    k += 1
                q.append((nr, nc))
    return [0, k] if k > v else [v, 0]
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
wolf, sheep = 0, 0
for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph[i][j] != '#':
            visited[i][j] = 1
            v, k = bfs(i, j)
            wolf += v
            sheep += k
print(sheep, wolf)
