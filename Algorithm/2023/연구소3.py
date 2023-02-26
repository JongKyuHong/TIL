from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
delta = ((0,1),(0,-1),(1,0),(-1,0))
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))

min_v = float('inf')
for combi in combinations(virus, M):
    visited = [[float('inf')]*N for _ in range(N)]
    q = deque()
    for c in combi:
        i, j = c
        visited[i][j] = 0
        q.append((i, j))
    max_v = 0
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] > visited[r][c] + 1 and graph[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                if graph[nr][nc] == 0:
                    max_v = max(max_v, visited[nr][nc])
                q.append((nr, nc))
    flag = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and visited[i][j] == float('inf'):
                flag = 1
                break
        if flag:
            break
    if not flag:
        min_v = min(max_v, min_v)
    
if min_v == float('inf'):
    print(-1)
else:
    print(min_v)