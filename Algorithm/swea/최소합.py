def dfs(y,x,sum_value):
    print(sum_value)
    global min_value
    if y == n-1 and x == n-1:
        min_value = min(min_value,sum_value)
        return min_value
    if min_value < sum_value:
        return
    nx = x + dx[0]
    ny = y + dy[0]
    if (0 <= nx < n) and (0 <= ny < n):
        dfs(ny,nx,sum_value+graph[ny][nx])
    nx -= dx[0]
    ny -= dy[0]    
    nx = x + dx[1]
    ny = y + dy[1]
    if (0 <= nx < n) and (0 <= ny < n):
        dfs(ny,nx,sum_value+graph[ny][nx])
        



for test_case in range(int(input())):
    n = int(input())
    dx = [0,1]
    dy = [1,0]
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [False] * n
    min_value = 131
    sum_value = graph[0][0]
    dfs(0,0,sum_value)
    print(f'#{test_case+1} {min_value}')





