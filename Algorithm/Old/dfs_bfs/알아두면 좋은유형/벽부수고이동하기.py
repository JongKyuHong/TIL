from collections import deque

delta = ((0,1),(0,-1),(1,0),(-1,0))
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[[0]*m for _ in range(n)] for _ in range(2)]
q = deque()
q.append((0,0,1,1))
res = float('inf')
while q:
    r,c,bomb,count = q.popleft()
    visited[bomb][r][c] = 1
    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if nr == n-1 and nc == m-1:
            res = min(res, count+1)
            continue
        if 0 <= nr < n and 0 <= nc < m and not visited[bomb][nr][nc]:
            if graph[nr][nc] == '0':
                visited[bomb][nr][nc] = 1
                q.append((nr,nc,bomb,count+1))
            else:
                if bomb:
                    visited[0][nr][nc] = 1
                    q.append((nr,nc,0,count+1))
if n == 1 and m == 1:
    print(1)
elif res ==float('inf'):
    print(-1)
else:
    print(res)