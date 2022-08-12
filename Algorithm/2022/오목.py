graph = [list(map(int, input().split())) for _ in range(19)]

delta = ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1))

res = 0
def dfs(r, c,visited, cnt, d,cr,cc):
    global res
    flag = 0
    if cnt == 5:
        nr = delta[d+4][0]+cr
        nc = delta[d+4][1]+cc
        if 0 <= nr < 19 and 0 <= nc < 19:
            if graph[nr][nc] == graph[r][c]:
                flag = 0
            else:
                flag = 1
        else:
            flag = 1
    nr = delta[d][0]+r
    nc = delta[d][1]+c
    if 0 <= nr < 19 and 0 <= nc < 19 and graph[nr][nc] == graph[r][c] and not visited[nr][nc]:
        flag = 0
        visited[nr][nc] = 1
        dfs(nr, nc, visited, cnt+1, d,cr,cc)
        visited[nr][nc] = 0
    if flag == 1:
        res = graph[r][c]
        return 

visited = [[0]*19 for _ in range(19)]

for i in range(19):
    for j in range(19):
        if graph[i][j]:
            visited[i][j] = 1
            for k in range(4):
                dfs(i,j,visited,1,k,i,j)
            visited[i][j] = 0
            if res:
                print(res)
                print(i+1, j+1)
                exit()
if res == 0:
    print(0)