import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
graph_sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        graph_sum[i][j] = graph[i-1][j-1] + graph_sum[i-1][j] + graph_sum[i][j-1] - graph_sum[i-1][j-1]
for _ in range(m):    
    x1, y1, x2, y2 = map(int, input().split())
    print(graph_sum[x2][y2] - graph_sum[x1-1][y2] - graph_sum[x2][y1-1] + graph_sum[x1-1][y1-1])