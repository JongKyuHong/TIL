from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1), (0,-1),(1,0),(-1,0))

def bfs(r, c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = dr+r
            nc = dc+c
            if 0 <= nr < n and 0 <= nc < m:
                if palace[nr][nc] == 1:
                    continue
                elif palace[nr][nc] == 2:
                    if visited[nr][nc] > visited[r][c] + 1:
                        visited[nr][nc] = visited[r][c] + 1
                        dist = abs((n-1)-nr)+abs((m-1)-nc)
                        if visited[n-1][m-1] > visited[nr][nc]+dist:
                            visited[n-1][m-1] = visited[nr][nc]+dist
                else:
                    if visited[nr][nc] > visited[r][c] + 1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr,nc))

n, m, t = map(int, input().split()) # 성의크기, 공주에게 걸린 저주의 제한시간
palace = [list(map(int, input().split())) for _ in range(n)]
visited = [[sys.maxsize]*m for _ in range(n)]
bfs(0, 0)
print(visited[n-1][m-1] if visited[n-1][m-1] <= t else 'Fail')