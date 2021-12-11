def dfs(idx, _sum):
    global res
    if _sum >= res:
        return
    if idx == n:
        res = _sum
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, _sum+factory[idx][i])
            visited[i] = 0


for test_case in range(int(input())):
    n = int(input())
    factory = [list(map(int,input().split())) for _ in range(n)]
    res = float('inf')
    visited = [0 for _ in range(n)]
    dfs(0, 0)

    print(f'#{test_case+1} {res}')



