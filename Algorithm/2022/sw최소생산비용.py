def dfs(r, value):
    global res
    if r == n-1:
        res = min(res, value)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(r+1, value+ graph[r+1][i])
            visited[i] = 0

for T in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')
    for i in range(n):
        visited = [0] * n
        visited[i] = 1
        dfs(0, graph[0][i])
    print(f'#{T+1} {res}')