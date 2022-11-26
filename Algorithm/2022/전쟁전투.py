from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(m)]
visited = [[0]*n for _ in range(m)] # 같은땅을 여러번 확인하지 않기 위함
delta = ((0,1),(0,-1),(1,0),(-1,0)) # 인접한 땅을 확인하기 위함

def bfs(r, c, value):
    q = deque()
    q.append([r,c])
    cnt = 1
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and graph[nr][nc] == value:
                visited[nr][nc] = 1
                q.append((nr, nc))
                cnt += 1
    return cnt

w_cnt = 0 # 아군 힘
b_cnt = 0 # 적군 힘
for i in range(m):
    for j in range(n):
        if not visited[i][j]: # 방문하지 않은 땅인경우
            cnt = bfs(i, j, graph[i][j])
            if graph[i][j] == 'W':
                w_cnt += cnt**2
            else:
                b_cnt += cnt**2
print(w_cnt, b_cnt)