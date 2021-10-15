def dfs(index, ans):
    global res
    if ans >= b:
        res = min(res, ans)
    for i in range(index+1, n):
        if not visited[i] and ans + s[i] < res:
            visited[i] = 1
            dfs(i, ans + s[i])
            visited[i] = 0


for test_case in range(int(input())):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    visited = [0] * n
    res = float('inf')
    for i in range(n):
        visited[i] = 1
        dfs(i, s[i])
        visited[i] = 0
    print(f'#{test_case+1} {res-b}')
    
