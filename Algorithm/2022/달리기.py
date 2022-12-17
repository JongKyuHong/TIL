from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
s_r, s_c, e_r, e_c = map(int, input().split())
delta = ((0,1),(0,-1),(1,0),(-1,0))
visited = [[float('inf')]*m for _ in range(n)]

def bfs(r, c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            for i in range(1, k+1):
                nr, nc = (i*dr)+r, (i*dc)+c
                if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == '.' and visited[nr][nc] > visited[r][c]:
                    if visited[nr][nc] == float('inf'):
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))
                else:
                    break

bfs(s_r-1, s_c-1)
print(visited[e_r-1][e_c-1] if visited[e_r-1][e_c-1] != float('inf') else -1)