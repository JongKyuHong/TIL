from collections import deque

delta = [(1,0),(-1,0),(0,-1),(0,1)]


def bfs(i, j):
    global cnt
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    array[i][j] = cnt

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                array[nx][ny] = cnt
                q.append([nx, ny])


def bfs2(z):
    global ans
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if array[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] > 0 and array[nx][ny] != z:
                    ans = min(ans, dist[x][y])
                    return
                if array[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 1
ans = float('inf')

for i in range(n):
    for j in range(n):
        if not visited[i][j] and array[i][j] == 1:
            bfs(i, j)
            cnt += 1

for i in range(1, cnt):
    bfs2(i)

print(ans)