from collections import deque
import sys 
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(s, e):
    q = []
    heapq.heappush(q, (0, 1))
    dist[1] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_cost, next_node in lst[node]:
            if [s, e] == [next_node, node] or [s, e] == [node, next_node]:
                continue
            d = next_cost + cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))
def bfs():
    q = deque()
    q.append(N)
    visited = set()
    removes = set()
    while q:
        node = q.popleft()
        for next_cost, next_node in lst[node]:
            if dist[node] == dist[next_node] + next_cost:
                removes.add((node, next_node))
                if next_node not in visited:
                    visited.add(next_node)
                    q.append(next_node)
    return removes

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    lst[x].append((z, y))
    lst[y].append((z, x))

dist = [INF] * (N+1)
dijkstra(-1, -1)

removes = bfs()
lst2 = [[] for _ in range(N+1)]

answer = 0
for remove in removes:
    start, end = remove
    dist = [INF] * (N+1)
    dijkstra(start, end)
    answer = max(answer, dist[N])
print(answer)



# 어떤 정점을 삭제하였을때 최단거리를 최대로 할 수 있는가
# 대충 생각했을때 최단거리의 경로 정보를 받아서 그쪽으로 못가는 경우에 얼마나 걸리는지 확인하면 되지않을까?
# 아니면 bfs로 경로 재추적이 가능했다. 
# 그것을 통해서 가능?



