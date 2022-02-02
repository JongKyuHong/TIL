from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

delta = ((0,1),(0,-1),(1,0),(-1,0))

nr, nc = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            nr, nc = i, j
            break

size = 2
move_num = 0
eat = 0
while 1:
    q = deque()
    q.append((nr,nc,0))
    visited = [[0] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        r,c,count = q.popleft()
        if count > flag:
            break
        for dr, dc in delta:
            nr,nc = r+dr, c+dc
            if nr < 0 or nc < 0 or nr >=n or nc >= n:
                continue
            if graph[nr][nc] > size or visited[nr][nc]:
                continue
            if graph[nr][nc] != 0 and graph[nr][nc] < size:
                fish.append((nr,nc,count+1))
                flag = count
            visited[nr][nc] = 1
            q.append((nr,nc,count+1))
    if len(fish) > 0:
        fish.sort()
        r, c, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        graph[r][c] = 0
        if eat == size:
            size += 1
            eat = 0
        nr, nc = r, c
    else:
        break
print(move_num)
