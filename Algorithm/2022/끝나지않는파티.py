from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 파티장의 크기, 서비스를 요청한 손님의 수
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


for i in range(m):
    a, b, c = map(int, input().split())

    if graph[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')