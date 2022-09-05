import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 아이스크림종류, 섞어먹으면 안되는 조합
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

res = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if not graph[i][j] and not graph[i][k] and not graph[j][k]:
                res += 1
print(res)