from collections import deque
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

graph = [input().rstrip() for _ in range(r)]
delta = ((0,1),(-1,0),(1,0),(0,-1))#,(1,0),(0,-1))
visited = [[0]*c for _ in range(r)]
cnt = 0
def dfs(x, y, dist):
    if x == 0 and y == c-1 and dist == k:
        global cnt
        cnt += 1
    for dr, dc in delta:
        nr, nc = dr+x, dc+y
        if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] != 'T' and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, dist+1)
            visited[nr][nc] = 0
visited[r-1][0] = 1
dfs(r-1, 0, 1)
print(cnt)