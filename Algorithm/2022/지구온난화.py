import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(i, j):
    answer = 0
    for dr, dc in delta:
        nr, nc = dr+i, dc+j
        if 0 <= nr < r and 0 <= nc < c:
            if graph[nr][nc] == '.':
                answer += 1
        else:
            answer += 1
    return answer

min_r, max_r, min_c, max_c = 11, -1, 11, -1
res = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            target = bfs(i, j)
            if target == 3 or target == 4:
                res.append((i,j))

for i, j in res:
    graph[i][j] = '.'

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            min_r = min(min_r, i)
            max_r = max(max_r, i)
            min_c = min(min_c, j)
            max_c = max(max_c, j)

for i in range(min_r, max_r+1):
    answer = ''
    for j in range(min_c, max_c+1):
        answer += graph[i][j]
    print(answer)