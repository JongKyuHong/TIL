delta = ((0,1),(0,-1),(1,0),(-1,0))

map1 = [
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
]

def bfs():
    q = []
    q.append((0,0))
    while q:
        x, y = q.pop()
        for dx, dy in delta:
            nx, ny = dx + x, dy + y
            if 0 <= nx < 4 and 0 <= ny < 5:
                if not map1[nx][ny]:
                    map1[nx][ny] = map1[x][y] + 1
                    q.append((nx, ny))
bfs()
print(map1)



