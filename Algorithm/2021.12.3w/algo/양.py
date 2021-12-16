from collections import deque
def bfs(r,c):
    global w, s
    q.append((r,c))
    while q:
        r, c = q.popleft()
        if graph[r][c] == 'v':
            w += 1
        elif graph[r][c] == 'o':
            s += 1
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != '#' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr,nc))

delta = ((0,1),(0,-1),(1,0),(-1,0))
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)] # .은 빈필드, # 울타리, v 늑대, o 양
visited = [[0]*m for _ in range(n)]
wolf, sheep = 0, 0
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] != '#' and visited[i][j] == 0:
            w, s = 0, 0
            visited[i][j] = 1
            bfs(i, j)
            if w >= s:
                s = 0
            else:
                w = 0
            wolf += w
            sheep += s
print(sheep, wolf)
                

        
            

