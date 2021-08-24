def dfs(y,x):
    global res
    array[y][x] = 1
    for step in range(4):
        nx = dx[step]+x
        ny = dy[step]+y
        if (0 <= nx < n) and (0 <= ny < n):
            if array[ny][nx] == 3:
                res = 1
                return
            if array[ny][nx] == 0:
                dfs(ny,nx)


dx = [0,-1,0,1]
dy = [-1,0,1,0]

for test_case in range(int(input())):
    n = int(input())
    array = [list(map(int,input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if array[i][j] == 2:
                x = j
                y = i
    res = 0
    dfs(y,x)
    print(f'#{test_case+1} {res}')
