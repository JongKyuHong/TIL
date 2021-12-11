# 한 지점에서 다른 특정 지점까지의 최단경로를 구해야 하는 경우

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(n+1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    while q:
        dist, now = heapq.heappop(q) # dist : 비용, now : 현재위치
        if distance[now] < dist: # distance에 저장된 값보다 dist값이 적으면 그냥넘김
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] < cost:
                distance[i[0]] = cost
                heapq.heappush(q,(distance[i[0]],i[0]))
dijkstra(start)
for i in range(1,n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])



