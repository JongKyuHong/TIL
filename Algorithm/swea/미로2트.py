def dfs(y,x):
    global res
    array[y][x] = 1  # 현재위치를 1로한다. 
    for step in range(4):  # 4가지 방향을 보기위해 range(4)
        nx = dx[step] + x
        ny = dy[step] + y
        if (0 <= nx < n) and (0<= ny < n):  # 새로 정한 방향이 문제가없고
            if array[ny][nx] == 0:  # 나아간곳이 빈곳이면
                dfs(ny,nx)  #거기부터 dfs시작
            if array[ny][nx] == 3:  # 나아간곳이 도착지이면
                res = 1
                return
            
t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    array = [list(map(int,input())) for _ in range(n)]
    dx = [0,1,-1,0] # 방향을 정함 위쪽, 오른쪽, 왼쪽, 아래
    dy = [-1,0,0,1]

    for i in range(n):
        for j in range(n):
            if array[i][j] == 2:  # 출발지점을 찾는다
                x = j
                y = i
                break
    res = 0
    dfs(y,x) # 출발지점 부터 dfs시작

    print(f'#{test_case} {res}')


