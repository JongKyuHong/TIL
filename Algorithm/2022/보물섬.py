from collections import deque
delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(r, c):
    res = 0 
    q = deque()
    q.append((r,c,1))
    visited[r][c] = 1
    while q:
        r, c, dist = q.popleft()
        res = max(res,dist)
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc] == 'L':
                visited[nr][nc] = 1
                q.append((nr,nc,dist+1))
    return res                

    
n,m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

result = 0
rr,cc=0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            cnt = bfs(i,j)
            if result < cnt:
                result = cnt
print(result-1)
        
