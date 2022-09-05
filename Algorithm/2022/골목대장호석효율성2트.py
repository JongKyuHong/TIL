import sys
import heapq

input = sys.stdin.readline

n, m, a, b, c = map(int, input().split()) # 교차로갯수, 골목갯수, 시작교차로번호, 도착교차로번호, 가진돈
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int, input().split()) # 
    graph[x].append((y,z))
    #graph[y].append((x,z))

dist = [0] * (n+1)
#dist[b] = sys.maxsize
ans = sys.maxsize
def find(v):
    global ans
    q = [[0, v]]
    
    while q:
        now_dist, now = heapq.heappop(q)
        if now_dist > c:
            continue
        if now == b:
            if now_dist <= c:
                ans = min(ans, dist[b])
        for next_node, next_dist in graph[now]:
            if dist[next_node] < next_dist:
                dist[next_node] = next_dist
            heapq.heappush(q, (next_dist+now_dist, next_node))
                
find(a)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)