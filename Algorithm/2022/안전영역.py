from collections import deque

n = int(input())
graph = []
maxNum = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] 

delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(r, c, rain):
    q = deque()
    q.append((r,c))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and graph[nr][nc] > rain:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
        
res = 0
for rain in range(maxNum):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                bfs(i, j, rain)
    res = max(res, cnt)
print(res)