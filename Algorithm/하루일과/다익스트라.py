## 다익스트라란 한 지점에서 다른 한 지점으로 넘어갈때 가장 최단거리로 가는 경로값을 나타내는것

import heapq
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드의 번호 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)


# 간선 정보 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heapush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for c, d in graph[now]:
            cost = dist + d
            if cost < distance[c]:
                distance[c] = cost
                heapq.heappush(q, (cost, c))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
        

