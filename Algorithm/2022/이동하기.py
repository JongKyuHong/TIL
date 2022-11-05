import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i < 1:
            if j < 1:
                continue
            else:
                graph[i][j] += graph[i][j-1]
        else:
            if j < 1:
                graph[i][j] += graph[i-1][j]
            else:
                graph[i][j] += max(graph[i-1][j], graph[i][j-1])
print(graph[n-1][m-1])