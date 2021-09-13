import heapq

v, e = map(int, input().split())
k = int(input())
INF = int(1e9)

graph = [[] * (v+1) for _ in range(v+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v+1)

# 간선 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    # a->b가 c비용
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])