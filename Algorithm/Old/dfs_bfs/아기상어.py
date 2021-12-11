from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            q.append((i,j,0))
            break
size = 2
delta = ((-1,0),(0,-1),(1,0),(0,1))
while q:
    r,c,dist = q.popleft()
    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < n:
            
            


