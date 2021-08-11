t = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for test_case in range(1,t+1):
    n = int(input())
    array = [[0]*n for _ in range(n)]
    x,y,step = 0,0,0
    for i in range(1,(n**2)+1):
        array[x][y] = i
        x = x+dx[step]
        y = y+dy[step]
        if x < 0 or y < 0 or x >= n or y >= n or array[x][y] != 0:
            x -= dx[step]
            y -= dy[step]
            step = (step+1)%4
            x = x+dx[step]
            y = y+dy[step]
    print(f'#{test_case}')
    for i in array:
        print(*i)




