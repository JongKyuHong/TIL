from collections import deque

def bfs(r,c,n,m,maps):
    delta = ((0,1),(0,-1),(1,0),(-1,0))
    visited = [[0]*m for _ in range(n)]
    q = deque()
    visited[r][c] = 1
    q.append((r,c,1))
    ans = 10001
    while q:
        r,c, dist = q.popleft()
        if r == n-1 and c == m-1:
            ans = min(ans, dist)
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr,nc, dist+1))
    if ans == 10001:
        return -1
    else:
        return ans          

def solution(maps):
    n = len(maps)
    m = 0
    for i in maps[0]:
        m += 1
    return bfs(0,0,n,m,maps)

## 전형적인 bfs문제인데 풀고나서 기분이 너무좋아서 업로드,,

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))