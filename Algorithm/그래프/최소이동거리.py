import heapq

for test_case in range(int(input())):
    n, e = map(int, input().split())
    distance = [0] + [float('inf') for _ in range(n)]
    node = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(e):
        a, b, c = list(map(int, input().split()))
        node[a].append((b, c))
    queue = []
    heapq.heappush(queue, (0, 0))
    while queue:
        d, idx = heapq.heappop(queue)
        if visited[a]:
            continue
        visited[idx] = 1
        for a, b in node[idx]:
            if distance[a] > d + b:
                distance[a] = d + b
                heapq.heappush(queue,(distance[a], a))
    print(f'#{test_case+1} {distance[n]}')






