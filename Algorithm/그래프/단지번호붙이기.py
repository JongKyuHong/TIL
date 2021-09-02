n = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
graph = [list(map(int,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def dfs(i, j, cnt):
    visited[i][j] = 1
    global nums
    if graph[i][j] == 1:
        nums += 1
    for i in range(4):
        ni = i + di[i]
        nj = j + dj[i]
        if 0 <= ni < n and 0 <= nj < n:
            if visited[ni][nj] == 0 and graph[ni][nj] == 1:
                dfs(ni,nj, cnt)


cnt = 1
numlist = []
nums = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j, cnt)
            numlist.append(nums)
            nums = 0
print(len(numlist))
for i in sorted(numlist):
    print(i)
