n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)]

delta = ((0,1),(0,-1),(1,0),(-1,0))
result = 0
def virus(r, c):
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if temp[nr][nc] == 0:
                temp[nr][nc] = 2
                virus(nr, nc)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1
dfs(0)
print(result)
