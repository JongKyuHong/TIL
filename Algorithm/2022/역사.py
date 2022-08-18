import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b =  map(int, input().split())
    graph[a][b] = -1
    graph[b][a] = 1


# graph[a][b] = -1 # a가 b보다 먼저일어남
# graph[a][c] = -1 # a가 c보다 먼저일어남
# graph[c][b] = -1 # c가 b보다 먼저 

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 0:
                if graph[i][k] != 0 and graph[k][j] != 0:
                    if graph[i][k] == graph[k][j]:
                        graph[i][j] = graph[i][k]

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    print(graph[a][b])
