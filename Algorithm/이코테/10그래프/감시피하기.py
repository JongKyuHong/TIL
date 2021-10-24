def dfs(count):
    global teacher, graph, result, wall
    if count > 3:
        return
    if count == 3:
        if check_t():
            result = 'YES'
            return
        else:
            result = 'NO'
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                wall.append((i,j))
                dfs(count+1)
                if result == 'YES':
                    return
                wall.remove((i, j))
                graph[i][j] = 'X'
    

def check_t():
    global teacher, graph
    for t in teacher:
        for dr, dc in delta:
            r, c = t
            while 0 <= r < n and 0 <= c < n:
                if graph[r][c] == 'O':
                    break
                elif graph[r][c] == 'S':
                    return False
                r += dr
                c += dc
    return True                

            
                


n = int(input())
graph = [list(input().split()) for _ in range(n)]
delta = ((0,1),(0,-1),(1,0),(-1,0))
count = 3
result = 'NO'
teacher = []
wall = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i,j))

dfs(0)
print(result)

