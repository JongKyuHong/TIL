from collections import deque

def bfs(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for test_case in range(int(input())):
    n, m = map(int, input().split()) # nxm크기의 격자
    array = []
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    for _ in range(n):
        array.append(input())
    for i in range(n):
        for j in range(m):
            if array[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 0
    bfs(q)
    res = 0
    for i in range(n):
        for j in range(m):
            res += visited[i][j]
    print(f'#{test_case+1} {res}')
