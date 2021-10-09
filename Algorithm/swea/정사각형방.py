dc = [0,0,-1,1]
dr = [-1,1,0,0]

def dfs(r, c):
    global result
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >=n or nc < 0 or nc >= n:
            continue
        if graph[nr][nc]-graph[r][c] == 1:
            result += 1
            dfs(nr, nc)
    return
        
    

for test_case in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    ans = 1
    start = 0
    for i in range(n):
        for j in range(n):
            result = 1
            dfs(i, j)
            if ans < result:
                ans = result
                start = graph[i][j]
            elif ans == result:
                if start > graph[i][j]:
                    start = graph[i][j]
    print(f'#{test_case+1} {start} {ans}')