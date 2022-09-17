import heapq

def dijkstra(start):
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            cost = next_dist + dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

for T in range(int(input())):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        s, e, w = map(int, input().split()) # 시작거리, 끝지점, 가중치
        graph[s].append((e, w))

    distance = [float('inf')] * (n+1)
    distance[0] = 0
    dijkstra(0)
    print(f'#{T+1} {distance[n]}')