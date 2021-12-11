def dfs(row,sum_value):
    global min_value
    if row == n:
        min_value = min(min_value,sum_value)
    if min_value < sum_value:
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
    min_value = 101
    sum_value = 0
    dfs(0,sum_value)
    print(f'#{test_case+1} {min_value}')

