def dfs(x, y):
    global ans
    if x < 0 or x >= n or y < 0 or y >= n or matrix[x][y] == '0':
        return
    if matrix[x][y] == 1:
        ans.append(matrix[x][y])
        matrix[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return
    return
    


n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        ans = []
        dfs(i, j)
        if ans:
            res.append(ans)
print(len(res))
for i in res:
    print(len(i))