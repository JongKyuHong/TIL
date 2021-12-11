import heapq

INF = float('inf')

def dijkstra(start):
        q = []
        heapq.heappush(1, (0,start))
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
    n, m, x = map(int, input().split())
    graph = [[] for _  in range(n+1)]

    for _ in range(m):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))
    distance = [INF] * (n+1)
    
    dijkstra(0)

    for i in range(1, n+1):
        if distance[i] == INF:
            


    