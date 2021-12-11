from collections import deque

def bfs(r, c):
    global check
    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < h and 0 <= nc < w and graph[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = check
                q.append((nr, nc))



while 1:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        exit()
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    check = 1
    delta = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]:
                visited[i][j] = check
                bfs(i,j)
                check += 1
    max_val = 0
    for i in visited:
        max_val = max(max_val, max(i))
    print(max_val)
    
