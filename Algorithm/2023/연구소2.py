from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
INF = float("inf")
delta = ((0,1),(0,-1),(1,0),(-1,0))

def check():
    value = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] != 1:
                if visited[i][j] == INF:
                    return INF
                else:
                    value = max(value, visited[i][j])
    return value

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            lst.append([i,j])
ans = INF
for per in combinations(lst, M):
    visited = [[INF]*N for _ in range(N)]
    max_v = 0
    q = deque()
    for p in per:
        i, j = p
        visited[i][j] = 0
        q.append((i, j))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] > visited[r][c] + 1 and lab[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    ans = min(ans, check())

print(ans if ans != INF else -1)

