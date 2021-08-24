def dfs(row,sum_value):
    global min_value
    if row == n:
        min_value = min(min_value, sum_value)
        return min_value
    
    if sum_value > min_value:
        return 
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(row+1,sum_value+graph[row][i])
            visited[i] = False



for test_case in range(int(input())):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    min_value = 100
    dfs(0,0)
    print(f'#{test_case+1} {min_value}')



