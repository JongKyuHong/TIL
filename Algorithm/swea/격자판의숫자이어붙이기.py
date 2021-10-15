dc = [0,0,-1,1]
dr = [-1,1,0,0]

def dfs(r, c, line):
    if len(line) == 7:
        ans.add(line)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        dfs(nr, nc, line+arr[nr][nc])

for test_case in range(int(input())):
    n = 4
    arr = [input().split() for _ in range(n)]
    ans = set()
    for i in range(n):
        for j in range(n):
            dfs(i, j, arr[i][j])

    print(f'#{test_case+1} {len(ans)}')