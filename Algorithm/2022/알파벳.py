r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
delta = ((0,1),(0,-1),(1,0),(-1,0))
visited = [0]*26 
#visited = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'W':0,'V':0,'X':0,'Y':0,'Z':0}
def dfs(x,y,count,visited):
    global res
    if count > res:
        res = count
    for dr, dc in delta:
        nr = x + dr
        nc = y + dc
        if 0 <= nr < r and 0 <= nc < c and not visited[65-ord(graph[nr][nc])]:
            visited[65-ord(graph[nr][nc])] = 1
            dfs(nr, nc,count+1,visited)
            visited[65-ord(graph[nr][nc])] = 0
visited[65-ord(graph[0][0])] = 1
res = 1
dfs(0,0,res,visited)
print(res)