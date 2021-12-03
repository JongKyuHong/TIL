from collections import deque
delta = ((-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

m, n, h  = map(int, input().split())
graph = []
q = deque()

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i,j,k])
    graph.append(tmp)

while q:
    x, y, z = q.popleft()
    for dx, dy, dz in delta:
        nx = dx + x
        ny = dy + y
        nz = dz + z
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            q.append([nx,ny,nz])
            graph[nx][ny][nz] = graph[x][y][z] + 1

day = 0
for i in graph:
    print(i)
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)
                