from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[0][a][b] = 0
    while q:
        a, b = q.popleft()
        for dr, dc in delta:
            nr = dr + a
            nc = dc + b
            if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] != 'X' and graph[nr][nc] != 'D':
                if visited[0][nr][nc] < 0:
                    visited[0][nr][nc] = visited[0][a][b] + 1
                    q.append((nr, nc))
                else:
                    if visited[0][nr][nc] > visited[0][a][b] + 1:
                        visited[0][nr][nc] = visited[0][a][b] + 1
                        q.append((nr, nc))

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)] # S시작점 D 도착점
start_r, start_c = 0, 0
end_r, end_c = 0, 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'D':
            end_r, end_c = i, j
        elif graph[i][j] == 'S':
            start_r, start_c = i, j

visited = [[[-1]*c for _ in range(r)] for _ in range(2)] # 0 물 1 고슴

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            bfs(i, j)

visited[0][end_r][end_c] = -1
q = deque()
q.append((start_r, start_c))
visited[1][start_r][start_c] = 0
res = sys.maxsize
while q:
    a, b = q.popleft()
    for dr, dc in delta:
        nr = dr + a
        nc = dc + b
        if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] != 'X':
            if nr == end_r and nc == end_c:
                res = min(res, visited[1][a][b] + 1)
                
            if visited[1][nr][nc] < 0:
                if visited[0][nr][nc] > visited[1][a][b] + 1:
                    visited[1][nr][nc] = visited[1][a][b] + 1
                    q.append((nr, nc))
                elif visited[0][nr][nc] == -1:
                    visited[1][nr][nc] = visited[1][a][b] + 1
                    q.append((nr, nc))


print('KAKTUS' if res == sys.maxsize else res)