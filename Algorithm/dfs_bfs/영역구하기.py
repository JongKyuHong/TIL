from collections import deque

delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(r, c):
    cnt = 1
    graph[r][c] = 1
    q = deque()
    q.append((r,c))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0 <= nr < m and 0 <= nc < n and not graph[nr][nc]:
                graph[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))
    return cnt
m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

res = []
for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            res.append(bfs(i, j))

print(len(res))
res.sort()
print(*res)


