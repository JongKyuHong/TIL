import sys
import heapq
input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y, z)) # 교차로 두개의 번호, 수금액
res = []
ans = sys.maxsize
dist = [sys.maxsize] * (n+1)
def find(start):
    global ans
    dist[start] = 0
    q = [[0, start, 0]]
    while q:
        now_dist, now, sum_v = heapq.heappop(q)
        if now == b and dist[now] <= c:
            print(dist[now], ';aa')
            ans = min(ans, sum_v)
            continue
        if dist[now] < now_dist:
            continue
        for next_node, next_dist in graph[now]:
            d = next_dist + now_dist
            if dist[next_node] > d:
                dist[next_node] = d
                sum_v = max(sum_v, next_dist)
                heapq.heappush(q, (d, next_node, sum_v))

res.append(0)
find(1)
print(-1 if ans == sys.maxsize else ans)