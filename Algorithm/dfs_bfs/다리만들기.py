def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if matrix[x][y] == 1:
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        dfs(i, j)


