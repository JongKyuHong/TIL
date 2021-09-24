dr = [0,1,0,-1]
dc = [1,0,-1,0]
connect = [2, 3, 0, 1] # 연결된 정보 담아놓은곳
#터널 구조물
pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0,1,0,1],
    [1,0,1,0],
    [1,0,0,1],
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
]

t = int(input())

for test_case in range(1,t+1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)] # 시간쳌 겸 방문 쳌
    q = [(r,c)]
    visited[r][c] = 1
    ans = 0
    while q:
        r,c = q.pop(0)
        ans += 1
        if visited[r][c] >= l: continue
        for d in range(4):
            curr_p = tunnel[r][c]
            if pipe[curr_p][d] == 0: continue
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 좌표가 맵을 벗어났다면
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            # 현재 바라보는 방향으로 길이 x
            

            #nd = (d+2)%4
            nd = connect[d]
            np = tunnel[nr][nc]
            
            # 방문을 했거나, 다음 좌표의 파이프가 현재좌표와 연결되지 않는다면
            if visited[nr][nc] or pipe[np][nd] == 0: continue
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr,nc))
    print(f'#{test_case} {ans}')
