import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


for test_case in range(int(input())):
    N, E = map(int, input().split())
    INF = float('inf')
    graph = [[] for _ in range(N)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e,w))
    
    distance = [INF] * (N+1)
    dijkstra(0)
    print(f'#{test_case+1} {distance[N]}')

    
