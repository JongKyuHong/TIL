import sys 
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF]*(N+1)
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        for next_cost, next_node in lst[node]:
            d = cost + next_cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))
    return dist


N, E = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    lst[a].append((c, b))
    lst[b].append((c, a))
v1, v2 = map(int, input().split())

dist_start_1 = dijkstra(1)
dist_start_v1 = dijkstra(v1)
dist_start_N = dijkstra(N)

answer = min(
dist_start_1[v1] + dist_start_v1[v2] + dist_start_N[v2],
dist_start_1[v2] + dist_start_v1[v2] + dist_start_N[v1])
print(answer if answer != INF else -1)



# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v1 -> N
# 위 두개중 뭐가 더 빠른가 보면 되는거 아닌가?

# 1에서 N으로 갈때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램
# 양방향길 이기때문에 뒤집어서 판단해도 같다.
# 1 -> v1 -> v2 -> N, 1 -> v2 -> v1 -> N 
# 1에서 출발하기 때문에 1 -> v1 -> 1 -> v2 -> N 이런거
# 1 -> v2 -> 1 -> v1 -> N 잠깐 그 친구만 들렀다가 오는거 가능한지?
# 4가지 경우를 비교해서 가장 짧은 것
# 다익스트라를 1과 N, v1 으로 돌려서 dist리스트 세개를 가지고 나머지 경우를 모두 판단가능

