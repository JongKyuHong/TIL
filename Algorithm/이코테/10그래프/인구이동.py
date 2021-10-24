from collections import deque
def bfs(r, c, index):
    q = deque()
    united = []
    united.append((r,c))
    q.append((r,c))
    union[r][c] = index
    summary = graph[r][c]
    count = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr + r , dc + c
            if 0 <= nr < n and 0 <= nc < n and union[nr][nc] == -1:
                if L <= abs(graph[nr][nc] - graph[r][c]) <= R:
                    q.append((nr, nc))
                    union[nr][nc] = index
                    summary += graph[nr][nc]
                    count += 1
                    united.append((nr,nc))
    for i, j in united:
        graph[i][j] = summary // count
                    
total_count = 0
n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

delta = ((0,1),(0,-1),(1,0),(-1,0))

while 1:
    index = 0
    union = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1
print(total_count)




