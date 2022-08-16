from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 파티장의 크기, 서비스를 요청한 손님의 수
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        graph[i][j] = data[j]

# for k in range(n):
#     for a in range(n):
#         for b in range(n):
#             if graph[i][j] > graph[i][k]+graph[k][j]:
#                 graph[i][j] = graph[i][k] + graph[k][j]


for i in range(m):
    a, b, c = map(int, input().split())
    for k in range(n):
        if graph[a-1][b-1] > graph[a-1][k] + graph[k][b-1]:
            graph[a-1][b-1] = graph[a-1][k] + graph[k][b-1]

    if graph[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')