
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def work(r, c, road, skill): # 좌표, 길이, 스킬
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            # 현 위치보다 낮은곳으로 이동할때
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road+1, skill)
            # 현위치보다 높거나 같은 곳으로 이동할 때
            elif skill and mountain[r][c] > mountain[nr][nc] - k:
                tmp = mountain[nr][nc] # 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road+1, 0) # 스킬사용
                mountain[nr][nc] = tmp # 원상복구
    visited[r][c] = 0 # 다음 경로를 위해 풀어준다



for test_case in range(int(input())):
    n, k = map(int, input().split())
    mountain = [list(map(int,input().split())) for _ in range(n)]
    max_h = 0
    for i in range(n):
        for j in range(n):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]
    
    visited = [[0]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == max_h:
                work(i, j, 1, 1)
    print(f'#{test_case+1} {ans}')

    


