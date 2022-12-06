import sys
input = sys.stdin.readline

n, m  = map(int, input().split())

graph = []
visited = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        visited[b][a] = 1
    else:
        visited[a][b] = 1

res = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        if not visited[i][j]:
            for k in range(j+1, n+1):
                if not visited[j][k] and not visited[i][k]:
                    res += 1

print(res)