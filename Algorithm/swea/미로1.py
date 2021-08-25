def dfs(y, x):
    global res
    for dy, dx in moves:
        ny = y + dy
        nx = x + dx
        if (0 <= nx < 16) and (0 <= ny < 16) and matrix[ny][nx] != 1:
            if matrix[ny][nx] == 3:
                res = 1
                return
            else:
                matrix[y][x] = 1
                dfs(ny,nx)
        ny -= dy
        nx -= dx



moves = ((1,0),(-1,0),(0,1),(0,-1))

for _ in range(10):
    tc = int(input())
    matrix = [list(map(int,input())) for _ in range(16)]
    dx = [1,-1,0,0]
    dy = []
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                start_y = i
                start_x = j
                break
            # elif j == 3:
            #     end_y = i
            #     end_x = j
    res = 0
    dfs(start_y, start_x)
    print(f'#{tc} {res}')
    






