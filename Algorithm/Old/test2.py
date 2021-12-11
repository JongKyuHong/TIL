delta = ((0,1), (0,-1), (1,0), (-1,0))
def bfs(x, y, val):
    q = [] 
    q.append((x,y))
    while q:
        val += 1
        x, y = q.pop()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 3:
                if graph[nx][ny]:
                    continue
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


graph = [[0]*3 for _ in range(4)]
graph[1][1] = 1
bfs(1, 1, 0)
print(graph[3][2])


