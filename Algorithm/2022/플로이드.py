import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[100001]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split()) # 시작도시, 도착도시, 비용
    if c < graph[a][b]:
        graph[a][b] = c
    #graph[a][b] = c
    

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 100001:
            print(0, end=' ')
        else:
            print(graph[i][j],end=' ')
    print()
