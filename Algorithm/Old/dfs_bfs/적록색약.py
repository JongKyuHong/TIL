from collections import deque

def normalbfs(r, c):
    q = deque()
    q.append((r,c))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r,dc+c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if graph[nr][nc] == color:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
        
    
def specialbfs(r,c):
    q = deque()
    q.append((r,c))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r,dc+c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if graph[nr][nc] == color:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                elif (graph[nr][nc] == 'R' or  graph[nr][nc] == 'G') and (color == 'R' or color == 'G'):
                    visited[nr][nc] = 1
                    q.append((nr, nc))

n = int(input())
graph = [input() for _ in range(n)]
normal = 0
special = 0
delta = ((0,1),(0,-1),(1,0),(-1,0))
check = 0
check1 = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = graph[i][j]
            normalbfs(i,j)
            check += 1

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = graph[i][j]
            specialbfs(i,j)
            check1 += 1
print(check, check1)
