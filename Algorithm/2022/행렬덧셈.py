import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        graph[i][j] += graph2[i][j]

for i in graph:
    print(*i)