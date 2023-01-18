import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float('inf')]*(n+1) for _ in range(n+1)]
path = [[[]]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    path[a][b] = [a, b]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(path[i][j]), *path[i][j])