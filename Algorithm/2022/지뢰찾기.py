import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
new_graph = [[0]*n for _ in range(n)]
delta = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1))

for i in range(n):
    for j in range(n):
        if graph[i][j].isdigit():
            new_graph[i][j] = -1
        else:
            for dr, dc in delta:
                nr, nc = i+dr, j+dc
                if 0 <= nr < n and 0 <= nc < n:
                    if graph[nr][nc].isdigit():
                        new_graph[i][j] += int(graph[nr][nc])

for i in range(n):
    target = ''
    for j in range(n):
        if new_graph[i][j] == -1:
            target += '*'
        elif new_graph[i][j] >= 10:
            target += 'M'
        else:
            target += str(new_graph[i][j])
    print(target)