import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 아이스크림 종류, 조합갯수
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

res = 0

for k in range(1, N+1):
    for i in range(k+1, N+1):
        for j in range(i+1, N+1):
            if not graph[i][j] and not graph[i][k] and not graph[k][j]:
                res += 1
print(res)