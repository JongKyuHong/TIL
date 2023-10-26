from itertools import combinations
from collections import deque
import sys 
input = sys.stdin.readline
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = float('inf')

def bfs(tmp):
    q = deque()
    visited =[[INF]*N for _ in range(N)]
    for r, c in tmp:
        q.append((r, c))
        visited[r][c] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] > visited[r][c] + 1 and lst[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
        
    max_v = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 0:
                max_v = max(max_v, visited[i][j])

    return max_v

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            virus.append((i, j))

answer = INF
for c in combinations(virus, M):
    answer = min(answer, bfs(c))

print(answer if answer != INF else -1)