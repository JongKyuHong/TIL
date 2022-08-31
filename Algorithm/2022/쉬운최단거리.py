from collections import deque
import sys
input = sys.stdin.readline
INF = float('inf')
delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(r, c):
    q = deque()
    q.append((r,c))
    while q:
        r, c =  q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 1:
                    if visited[nr][nc] > visited[r][c] + 1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))
                elif graph[nr][nc] == 0:
                    visited[nr][nc] = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 0은 갈수 없는 땅, 1은 갈수있는땅, 2는 목표지점
flag = 0
r, c = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            r, c = i, j 
            flag = 1
            break
    if flag:
        break

visited = [[INF]*m for _ in range(n)]
visited[r][c] = 0
bfs(r, c)

for i in range(n):
    for j in range(m):
        if visited[i][j] == INF:
            if graph[i][j] == 0:
                print(0, end=' ')
            else:
                print(-1, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()