from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))
R, C = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(R)]
start = []
fire_start = []
for i in range(R):
    for j in range(C):
        if lst[i][j] == 'J':
            start = [i, j]
        elif lst[i][j] == 'F':
            fire_start.append([i, j])

visited = [[float('inf')]*C for _ in range(R)]
q = deque()
for i,j in fire_start:
    q.append((i, j))
    visited[i][j] = 1
while q:
    r, c = q.popleft()
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == float("inf") and lst[nr][nc] != '#':
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

q.append(start)
visited[start[0]][start[1]] = 1
if start[0] == 0 or start[0] == R-1 or start[1] == 0 or start[1] == C-1:
    print(1)
    exit()
ans = float('inf')
while q:
    r, c = q.popleft()
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] != '#':
            if visited[nr][nc] > visited[r][c] + 1:
                visited[nr][nc] = visited[r][c] + 1
                if nr == 0 or nr == R-1 or nc == 0 or nc == C-1:
                    ans = min(ans, visited[nr][nc])
                else:
                    q.append((nr, nc))
print(ans if ans != float('inf') else 'IMPOSSIBLE')
