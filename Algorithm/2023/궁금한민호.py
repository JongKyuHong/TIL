import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dist = [[1]*N for _ in range(N)]
for k in range(N):
    for i in range(N):
        if i == k:
            continue
        for j in range(N):
            if i == j or j == k:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                print(-1)
                exit()
            elif graph[i][j] == graph[i][k] + graph[k][j]:
                dist[i][j] = 0
ans = 0
for i in range(N):
    for j in range(i, N):
        if dist[i][j]:
            ans += graph[i][j]
print(ans)