import sys
input = sys.stdin.readline

delta = ((0,1), (0,-1),(1,0),(-1,0))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

maxValue = 0

def dfs(r, c, dsum, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return
    
    for dr, dc in delta:
        nr = r+dr
        nc = c+dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, dsum+graph[nr][nc], cnt+1)
            visited[nr][nc] = 0

def exce(r, c):
    global maxValue
    for n in range(4):
        tmp = graph[r][c]
        for k in range(3):
            t = (n+k)%4
            nr = r+delta[t][0]
            nc = c+delta[t][1]

            if not (0 <= nr < N and 0 <= nc < M):
                tmp = 0
                break
            tmp += graph[nr][nc]
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = 0
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = 1

        exce(i, j)
print(maxValue)