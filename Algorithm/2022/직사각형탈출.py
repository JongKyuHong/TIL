from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c):
    q = deque()
    q.append((r,c,0))
    visited[r][c] = 1
    while q:
        r, c, dist = q.popleft()
        if r == fr-1 and c == fc-1:
            return dist
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr and nr+h-1 < n and 0 <= nc and nc+w-1 < m and not visited[nr][nc] and check(nr,nc):
                visited[nr][nc] = 1
                q.append((nr, nc, dist+1))
    return -1
def check(r, c):
    for i, j in wall:
        if r<=i<r+h and c<=j<c+w:
            return 0
    return 1

n, m = map(int, input().split()) # 격자판 크기
graph = []
wall = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j]:
            wall.append((i, j))
    graph.append(data)   

h,w,sr,sc,fr,fc = map(int, input().split()) # 직사각형크기 h, w and 시작좌표, 도착좌표
visited = [[0]*m for _ in range(n)]
INF = sys.maxsize
print(bfs(sr-1, sc-1))