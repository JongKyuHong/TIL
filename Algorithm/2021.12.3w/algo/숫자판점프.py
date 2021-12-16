def dfs(r,c,res):
    if len(res) == 6:
        if res not in visited:
            visited.append(res)
            return
    else:
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                dfs(nr,nc,res + str(graph[nr][nc]))
        return    
    
delta = ((0,1),(0,-1),(1,0),(-1,0))
graph = [list(map(int, input().split())) for _ in range(5)]
visited = []
for i in range(5):
    for j in range(5):
        res = ''
        dfs(i,j,res)
print(len(visited))
