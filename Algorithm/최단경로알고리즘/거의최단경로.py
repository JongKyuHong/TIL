from collections import deque
import sys
import heapq 
input = sys.stdin.readline
INF = float('inf')

def dijkstra():
    q = []
    heapq.heappush(q, (0, S))
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_cost, next_node in lst[node]:
            d = next_cost + cost
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(q, (d, next_node))

def bfs():
    q = deque()
    visited = set()
    q.append(D)
    removes = set()
    while q:
        now = q.popleft()
        if now == S:
            continue
        for next_cost, next_node in lst2[now]:
            d = dist[next_node] + next_cost
            if d == dist[now]:
                removes.add((next_node, now))
                if next_node not in visited:
                    q.append(next_node)
                    visited.add(next_node)
    return removes

while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())

    lst = [[] for _ in range(N)]
    lst2 = [[] for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        lst[U].append((P, V))
        lst2[V].append((P, U))
    
    dist = [INF]*N
    
    dijkstra()
    removes = bfs()
    new_lst = [[] for _ in range(N)]
    
    for i in range(N):
        for next_cost, next_node in lst[i]:
            if (i, next_node) not in removes:
                new_lst[i].append((next_cost, next_node))
    lst = new_lst

    dist = [INF] * N
    dijkstra()

    if dist[D] == INF:
        print(-1)
    else:
        print(dist[D])


# 최단 경로에 포함되지않는 경로 중 가장 짧은 경로를 구함
# 대충 생각했을때 최단경로를 구함 ( 경로중 지나왔던 부분과 길이)
# 그 다음에 최단경로길이와 같은 길이가 존재하는지 다시 다익스트라를 돌려서 찾음
# 없으면 마지막으로 한번더 돌려봐서 경로 찾음
# 시간초과

# 다익스트라를 계속돌리는게 시간초과의 원인인것 같다.
# 다익스트라를 최대한 덜 돌리고 경로를 찾는법?
# 처음에 돌릴때 최단 거리를 가진 모든 경로를 한번에 리턴한다
# 그리고 다익스트라를 돌려서 판단
# 75%에서 틀렸다. 엣지 케이스에서 틀리는것 같다.

# 풀이
# bfs를 통해 경로를 역추적하는 방법
# 생각도 못했던것 같다.