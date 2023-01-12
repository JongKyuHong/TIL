import sys
import heapq
input = sys.stdin.readline

N, R = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int, input().split()) # a번노드, b번노드, 길이가 d
    tree[a].append((b,d))
    tree[b].append((a,d))

def dijkstra(start):
    q = [[0, start]]
    dist = [float('inf')]*(N+1)
    dist[start] = 0
    target_node = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        if node == R:
            if len(tree[node]) >= 2 and target_node == 0:
                target_node = node
        else:
            if len(tree[node]) >= 3 and target_node == 0:
                target_node = node
        for next_node, next_cost in tree[node]:
            if next_cost + cost < dist[next_node]:
                dist[next_node] = next_cost + cost
                heapq.heappush(q, (dist[next_node],next_node))
    return target_node, dist

target_node, dist = dijkstra(R)
if target_node == 0:
    value = 0
    for i in range(1, N+1):
        if dist[i] != float('inf'):
            value = max(value, dist[i])
    print(value, 0)
elif target_node == R:
    value = 0
    for i in range(1, N+1):
        if dist[i] != float('inf') and i != R:
            value = max(value, dist[i])
    print(0, value)
else:
    #target_value = dist[target_node]
    #t, dist = dijkstra(target_node)
    value = 0
    for i in range(1, N+1):
        if dist[i] != float('inf') and i != R:
            value = max(value, dist[i])
    #print(target_value, value)
    print(dist[target_node], value-dist[target_node])
