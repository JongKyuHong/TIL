def dfs(y,x):
    global res
    data[y][x] = 1  # 일단 들어오자마자 현재위치 방문표시(1로바꿈)
    for d in range(4):
        nx = dx[d] + x  # 방향값을 더해준다,
        ny = dy[d] + y
        if (0 <= nx < n) and (0<= ny <n):  # 미로에서 벗어나지않았다면
            if data[ny][nx] == 0:  # 아직 방문하지 않은곳이면 dfs재호출
                dfs(ny,nx)
            if data[ny][nx] == 3:  # 다음장소가 도착지라면 리턴
                res = 1
                return

t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    data = [list(map(int,input())) for _ in range(n)]  # 미로생성
    dx = [1,-1,0,0]  # 방향 저장
    dy = [0,0,1,-1]  
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:  # 2의 위치를 찾음 (시작위치)
                x = j
                y = i
                break
    res = 0
    dfs(y,x)  # dfs함수 호출

    print(f'#{test_case} {res}')



