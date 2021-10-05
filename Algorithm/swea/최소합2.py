def dfs(x, y, val):
    global res
    if x == n-1 and y == n-1:
        if res > val:
            res = val
        return
    for i in range(2):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx > n-1 or ny > n-1:
            continue
        dfs(nx, ny, val+array[ny][nx])


for test_case in range(int(input())):
    n = int(input())
    dx = [1, 0]
    dy = [0, 1]
    array = [list(map(int, input().split())) for _ in range(n)]
    val = 0
    res = 99999999
    dfs(0, 0, array[0][0])
    print(f'#{test_case+1} {res}')