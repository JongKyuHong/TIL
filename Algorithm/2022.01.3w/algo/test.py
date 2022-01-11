# 데스나이트
from collections import deque
delta = ((-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1))
def bfs(r1,c1):
    q = deque()
    maxdist = 0
    q.append((r1,c1,0))
    visited[r1][c1] = 1
    while q:
        r, c, dist = q.popleft()
        if r == r2 and c == c2:
            maxdist = max(dist, maxdist)
            return maxdist
        for dr ,dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr,nc,dist+1))
              
n = int(input())
graph = [[0]*n for _ in range(n)]
r1,c1,r2,c2 = map(int, input().split())
visited = [[0]*n for _ in range(n)]
res = bfs(r1,c1)
if res:
    print(res)
else:
    print(-1)


